languages = ['C', 'CPP', 'JAVA', 'PYTHON', 'PERL', 'PHP', 'RUBY', 'CSHARP', 'HASKELL', 'CLOJURE', 'BASH', 'SCALA', 'ERLANG', 'CLISP', 'LUA', 'BRAINFUCK', 'JAVASCRIPT', 'GO', 'D', 'OCAML', 'R', 'PASCAL', 'SBCL', 'DART', 'GROOVY', 'OBJECTIVEC']

re_pattern = r"^[0-9]{4,5}\s[a-zA-Z]+"

import re

N = int(input())

str_list = []
for i in range (N):
    str_list.append(str(input()))
    
for i in range (N):
    string = re.findall(re_pattern, str_list[i])
    
    api_id, lan = string[0].split()
    
    if (lan in languages):
        print("VALID")
    else:
        print("INVALID")

        