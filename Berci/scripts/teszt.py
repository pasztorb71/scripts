import re

s = "CHECK (((format)::text = ANY (ARRAY[('PDF'::character varying)::text, ('TEXT'::character varying)::text])))"
pattern = r"ARRAY\[(.*?)\]"
array_text = re.search(pattern, s).group(1)
possible_values = re.findall(r"'(.*?)'", array_text)
print(possible_values)
print(array_text)