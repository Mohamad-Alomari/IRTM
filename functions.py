class preprocess: 
    def remove_stop_words(text):
        filtered_sentence= []
        for w in text: 

            if w not in stop_words: 
                filtered_sentence.append(w) 

        return filtered_sentence

    def stemming(text):
        stemmed_sentence= []
        for w in text: 
            w_stemming = ps.stem(w)
            stemmed_sentence.append(w_stemming) 
        return stemmed_sentence

    def clean_text(text):
        text_nonum = re.sub(r'\d+', '', text)

        text_nopunct = "".join([char.lower() for char in text_nonum if char not in string.punctuation]) 
  
        text_no_doublespace = re.sub('\s+', ' ', text_nopunct).strip()
        return text_no_doublespace

    
class collect_lines:
    def get_seasons_line(season):
        directory = r'script'
        for filename in os.listdir(directory):
            if filename.endswith(".txt"):
                if filename.startswith(season):
                    print(filename)
                    data = open(f"{directory}/{filename}", "r") 
                    text_first = data.read()
                    text = "\n".join([ll.rstrip() for ll in text_first.splitlines() if ll.strip()])
                    tt = text.split("\n")
                    for t in tt[1:]:
                        try:
                            (speaker, dialogue) =  t.split(":")
                            speaker = speaker.strip()
                            speaker = speaker.split("(")[0].strip()
                            if speaker in main_char:
                                tokenizer = RegexpTokenizer(r'\w+')
                                words = tokenizer.tokenize(dialogue.lower())
                                filtered_sentence = dialogue.lower()
                                filtered_sentence = remove_stop_words(words)
                                filtered_sentence = stemming(filtered_sentence)
                                if len(str(filtered_sentence)) != 0:
                                    #print('yes')
                                    lines[speaker][str(season)].append(filtered_sentence)
                        except ValueError:
                            pass
                        
    def get_seasons_line2(season):
        directory = r'script'
        for filename in os.listdir(directory):
            if filename.endswith(".txt"):
                if filename.startswith(season):
                    print(filename)
                    data = open(f"{directory}/{filename}", "r") 
                    text_first = data.read()
                    text = "\n".join([ll.rstrip() for ll in text_first.splitlines() if ll.strip()])
                    tt = text.split("\n")
                    for t in tt[1:]:
                        try:
                            (speaker, dialogue) =  t.split(":")
                            speaker = speaker.strip()
                            speaker = speaker.split("(")[0].strip()
                            if speaker in main_char:
                                filtered_sentence = preprocess.clean_text(dialogue)
                                if len(str(filtered_sentence)) != 0:
                                    #print('yes')
                                    lines[speaker][str(season)].append(filtered_sentence)
                        except ValueError:
                            pass