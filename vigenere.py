letter_index = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

text = "JRDMCQLEGASNAHSHJEVWAVGJSUDWPNUPELWGUAJFZWQRFXVWMWNNIZZWYFKMCMLIKWVCQUIQWGRGHXBYVAXZMRXILQUMGSXIWFWRFGOZWYAWJOQKTBMVVWLVRLVADSMYJIMIJUHSFLMNSHKEVMRJNAXPZWYIWHEXWVFWZEZSRPWITLWPBYMQCWTBMVDMUSQWVCMEIFKEGMKIPJITJJEIGTOCJZBLVELWXRJQIVSXVGRLIUVLHXOOJECZMEMKXHFERBSRPAINYMMEWQOVLINDENBAUHAXENWPVUMTILMBFWVWMWZSMTZAWRRQAQFXRFENBDIFTESMKHHULINXVREINBVIIAKEVWVRUISGKXREIAMLIVFZEVLINMWEQRMREISQWGYWFRINSCGYRINSVJTEZUIPWQYALIEWPAKJCCLENIDCFWHEUSRQWHETSTNLMEVUISWPIKAXNLMOVKZBMWADWDYWWCWETRLINKWWAWGEAKEVJISXGYEUSNBARHWVDIFWPWXTMNSVWFRINSRFGOZW"

french_freq = {
    'A':0.07636,'B':0.00901,'C':0.03260,'D':0.03669,'E':0.14715,'F':0.01066,
    'G':0.00866,'H':0.00737,'I':0.07529,'J':0.00613,'K':0.00049,'L':0.05456,
    'M':0.02968,'N':0.07095,'O':0.05344,'P':0.03056,'Q':0.01362,'R':0.06693,
    'S':0.07948,'T':0.07244,'U':0.06311,'V':0.01838,'W':0.00074,'X':0.00427,
    'Y':0.00128,'Z':0.00326
}

def calc(text_i):
    N = len(text_i)
    nb_letter = [0 for i in range(26)]
    for x in text_i:
        for i in range(26):
            if x == letter_index[i]:
                nb_letter[i] +=1

    IC = 0

    for i in range(26):
        IC = IC + nb_letter[i]*(nb_letter[i]-1)
    if (N <= 1):
        return 0
    IC = IC /(N*(N-1))
    return IC

#print(calc(text)) #print 0.04280178837555887

def ic_of_subseq(text_i, k):
    N = len(text_i)
    sub_texts = []

    for i in range(int(N/k)):
        sub_texts.append(calc(text_i[i::k]))

    avg = 0
    N_sub = len(sub_texts)
    for i in range(N_sub):
        avg = avg + sub_texts[i]
    return avg / N_sub

best_ic = ic_of_subseq(text,1)
for k in range(2,len(text)):
    N_text = len(text)
    value = ic_of_subseq(text,k)
    if abs(value-0.0778) < abs(best_ic-0.0778):
        best_ic = value
        best_k = k

#for k in range(2,len(text)):
    #print(ic_of_subseq(text,k))

print(ic_of_subseq(text,7))
print(best_ic)
print(best_k)

def index(letter):
    for index in range(26):
        if letter_index[index] == letter:
            return index
    return

def letter_counter(subtext):
    table_of_letters = [0]*26
    for ch in subtext:
        j = index(ch)
        table_of_letters[j] += 1
    return table_of_letters

def unshift(counts, shift):
    N = 0
    for x in counts:
        N += x

    chi = 0.0
    for p in range(26):
        expected = french_freq[letter_index[p]] * N
        c_idx = (p + shift) % 26
        observed = counts[c_idx]
        chi += (observed - expected) * (observed - expected) / expected
    return chi

key_shifts = []
key_letters = []
for j in range(best_k):
    col = text[j::best_k]
    c = letter_counter(col)

    best_shift = 0
    best_score = unshift(c, 0)
    for shift in range(1, 26):
        sc = unshift(c, shift)
        if sc < best_score:
            best_score = sc
            best_shift = shift

    key_shifts.append(best_shift)
    key_letters.append(letter_index[best_shift])

key = ""
for x in key_letters:
    key += x
print("key is :", key)

def decrypt_vigenere(crypted_text, key_shifts):
    k = len(key_shifts)
    message = []
    pos = 0
    for letter in crypted_text:
        letter_idx = index(letter)
        shift = key_shifts[pos % k]
        letter_shifted = (letter_idx - shift) % 26
        message.append(letter_index[letter_shifted])
        pos += 1
    return message

decrypted_message = decrypt_vigenere(text, key_shifts)
print(decrypted_message)