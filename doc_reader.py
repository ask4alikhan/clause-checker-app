Tesseract: 
This fetches the sections =>(Section.*?\\n\\n)
This fetches before + all sections w/positive lookahead => .*?(?=(Section.*?\\n\\n))
This fetches the after sections bit => \\n\\n\[.*
----