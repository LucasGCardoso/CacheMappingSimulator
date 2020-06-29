"""
mapeamento_direto.py: This file is responsible for simulating a direct mapping in a cache.

Configurations: The variables you should change in order to change the cache configuration:
 @param num_linhas: "Number of lines the cache should have"
 @param num_palavras: "Number of words the cache should have in each line"
 @param tag: "The number of bits the tag has in each address"
 @param linha: "The number of bits the line has in each address - only change the raw number, it must always sum with the tag"
 @param palavra: "The number of bits the words have in each address - only change the raw number, it must always sum with the linha variable"
"""
__author__      = "Lucas Cardoso, Pedro Rogoski"

######################
# Initializing cache #
######################
cache = []
num_linhas = 8
num_palavras = 8
num_colunas = 1 + num_palavras #The number 1 is the tag field

cache = [ [ 0 for i in range(num_colunas) ] for j in range(num_linhas) ]

###########################
#Taking the memory access #
###########################
memory_access = []
f = open("memory_access.txt", "r")
for x in f:
    for item in x.split(','):
        memory_access.append(item)

#####################################
# Initializing the cache properties #
#####################################

tag = 9 # number of bits in tag
linha = tag + 3 # number of bits in line
palavra = linha + 3 # number of bits in word
sel = palavra + 1 # number of bits in selector (it will always be 1)
num_of_bits = 16  #words of 16 bits
word_possibility_8 = ["000", "001", "010", "011", "100", "101", "110", "111"]
word_possibility_16 = ["0000", "0001", "0010", "0011", "0100", "0101", "0110", "0111", 
                        "1000", "1001", "1010", "1011", "1100", "1101", "1110", "1111",]


if(num_linhas == 8):
    words = word_possibility_8
    words_add = word_possibility_8
if(num_linhas == 16):
    words = word_possibility_16
    words_add = ["00", "01", "10", "11"]

miss_hit_list = []

##################################
# Iterating in the memory access #
##################################

for item in memory_access:
    # Transforming hexa to binary
    binary = bin(int(item, 16))[2:].zfill(num_of_bits)
    # Dividing the binary word in tag, line, word and selector bit
    t = 0
    bin_tag = ""
    bin_linha = ""
    bin_palavra = ""
    selector_bit = ""

    #we get the tag
    for i in range(tag):
        bin_tag += binary[i]

    #we get the line
    for i in range(tag, linha):
        bin_linha += binary[i]

    #we get the word
    for i in range(linha, palavra):
        bin_palavra += binary[i]

    #we get the selector bit
    for i in range(palavra, sel):
        selector_bit += binary[i]

    line = words.index(bin_linha)
    hit = False
    if(bin_tag == cache[line][0]):
        # we found the tag in the right line, so let's verify if the word is there
        for i in range(num_palavras):
            if(cache[line][i+1][linha:palavra] == bin_palavra):
                miss_hit_list.append('H')
                hit = True
                break

    if(hit == False):
        # It's a miss, so let's add the tag and the possible words in the cache
        miss_hit_list.append('M')
        cache[line][0] = bin_tag

        for i in range(num_palavras):
            value = bin_tag + bin_linha + words_add[i] + selector_bit
            cache[line][i+1] = value

###################################################
# End of main Script, Calculating misses and hits #
###################################################

misses = 0
hits = 0

for char in miss_hit_list:
    if(char == 'M'):
        misses += 1
    else:
        hits += 1

######################################
# Transforming from bin to hex again #
######################################
for i in range(num_linhas):
    for k in range(num_colunas):
        if(cache[i][k] != 0):
            decimal_representation = int(cache[i][k], 2)
            cache[i][k] = hex(decimal_representation)

########################
#  Showing the Results #
########################
if(num_linhas == 8):
    print("\n Mostrando resultados da primeira configuração - (cache de 8 linhas de 8 palavras) \n")
else:
    print("\n Mostrando resultados da segunda configuração - (cache de 16 linhas de 4 palavras) \n")

print("Número de hits: ", hits)
print("Número de misses: ", misses)
print("Percentual de hits (em %): ", ((hits * 100) / 289))
print("\n Conteúdo final da cache \n")
print("Tag      Data ")
for i in range(num_linhas):
    print(cache[i])