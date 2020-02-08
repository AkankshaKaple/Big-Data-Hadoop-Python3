%default INPUT '/home/hduser/Pig/Word_Count/in.txt';
%default OUTPUT '/home/hduser/Pig/Word_Count/output';
record = LOAD '$INPUT';
tokens = FOREACH record GENERATE FLATTEN(TOKENIZE((chararray) $0)) AS word;
grouped_tokens = GROUP tokens BY word;
count = FOREACH grouped_tokens GENERATE COUNT(tokens), group;
STORE count INTO '$OUTPUT';
