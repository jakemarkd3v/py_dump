import re
sample_text = 'The quick brown fox jumps over the lazy dog'

pattern = ['fox', 'fox', 'dog']

for pattern in pattern:
    print('Matching "%s" in pattern "%s" -->' % (pattern, sample_text))
    if re.search(pattern, sample_text):
    
      print('Matched!')
    
    else:
       print('Not Matched!')
    

