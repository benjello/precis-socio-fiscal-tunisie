-- Espaces insécables du français, posées au rendu pour que le texte source reste ordinaire.
-- Une espace devient insécable :
--   * entre deux groupes de chiffres d'un nombre (« 12 300 », « 1 234 567 ») ;
--   * avant « % » ;
--   * après « n° », « p. », « pp. », « art. » lorsqu'un chiffre suit ;
--   * à l'intérieur des guillemets français (« … ») et avant « : », « ; », « ! », « ? ».
-- Le code et les blocs bruts ne sont pas touchés (le filtre ne lit que les Inlines).
local NBSP = "\u{00A0}"

local function texte(el) return el and el.t == "Str" and el.text or nil end

local function insecable(a, b)
  local g, d = texte(a), texte(b)
  if g and d then
    if g:match("^%d%d?%d?$") and d:match("^%d%d%d[^%d]*$") then
      return true
    end
    if d:match("^%%") or d == "»" or d:match("^[:;!?]$") then return true end
    if g == "«" then return true end
    if (g == "n°" or g == "p." or g == "pp." or g == "art.") and d:match("^%d") then return true end
  elseif b and b.t == "Str" and (b.text == "»" or b.text:match("^[:;!?]$") or b.text:match("^%%")) then
    return true
  elseif a and a.t == "Str" and a.text == "«" then
    return true
  end
  return false
end

function Inlines(inlines)
  local change = false
  for i = 2, #inlines - 1 do
    if inlines[i].t == "Space" and insecable(inlines[i - 1], inlines[i + 1]) then
      inlines[i] = pandoc.Str(NBSP)
      change = true
    end
  end
  if change then return inlines end
end
