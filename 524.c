char* findLongestWord(char* s, char** dictionary, int dictionarySize) {
    char* result = NULL;
    int maxLength = 0;
    int sLen = strlen(s);
    
    for (int i = 0; i < dictionarySize; i++) {
        char* word = dictionary[i];
        int wordLen = strlen(word);
        
        // Verifica se a palavra pode ser formada de S
        int j = 0; // Ponteiro para S
        int k = 0; // ponteiro para a Palavra
        
        while (j < sLen && k < wordLen) {
            if (s[j] == word[k]) {
                k++;
            }
            j++;
        }
        
        // Se processarmos todos os caracteres da palavra, ela poderá ser formada
        if (k == wordLen) {
            // Se o resultado for NULL ou a palavra for maior, ou tiver o mesmo tamanho, mas for lexicograficamente menor
            if (result == NULL || wordLen > maxLength || (wordLen == maxLength && strcmp(word, result) < 0)) {
                result = word;
                maxLength = wordLen;
            }
        }
    }
    
    // Se nenhuma palavra for encontrada, retorne uma string vazia
    if (result == NULL) {
        char* emptyStr = (char*)malloc(1);
        emptyStr[0] = '\0';
        return emptyStr;
    }
    
    // Retorna uma cópia do resultado
    char* finalResult = (char*)malloc(strlen(result) + 1);
    strcpy(finalResult, result);
    return finalResult;
}