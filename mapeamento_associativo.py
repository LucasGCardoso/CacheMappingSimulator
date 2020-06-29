"""
mapeamento_associativo.py: This file is responsible for simulating an associative mapping in a cache.

Configurations: The variables you should change in order to change the cache configuration:
 @param num_linhas: "Number of lines the cache should have"
 @param num_palavras: "Number of words the cache should have in each line"
 @param tag: "The number of bits the tag has in each address"
 @param palavra: "The number of bits the words have in each address - only change the raw number, it must always sum with the tag"
"""
__author__      = "Lucas Cardoso"

######################
# Initializing cache #
######################
cache = []
num_linhas = 16
num_palavras = 4

num_colunas = 1 + num_palavras #The number 1 is the tag field

pointer = 0 #Variable that points to the next free line of the cache

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

tag = 13 # number of bits in tag
palavra = tag + 2 # number of bits in word
sel = palavra + 1 # number of bits in selector (it will always be 1)

NUM_OF_BITS = 16  #words of 16 bits - this is a constant and must not be changed

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
    binary = bin(int(item, 16))[2:].zfill(NUM_OF_BITS)
    # Dividing the binary word in tag, line, word and selector bit
    t = 0
    bin_tag = ""
    bin_palavra = ""
    selector_bit = ""

    #we get the tag
    for i in range(tag):
        bin_tag += binary[i]

    #we get the word
    for i in range(tag, palavra):
        bin_palavra += binary[i]

    #we get the selector bit
    for i in range(palavra, sel):
        selector_bit += binary[i]

    hit = False
    for i in range(num_linhas):
        if(cache[i][0] == bin_tag):
        # we found the tag in the cache, so let's verify if the word is really there
            for k in range(num_palavras):
                if(cache[i][k+1][tag:palavra] == bin_palavra):
                    miss_hit_list.append('H')
                    hit = True
                    break
            break

    if(hit == False):
        # It's a miss, so let's add the tag and the possible words in the cache
        miss_hit_list.append('M')
        cache[pointer][0] = bin_tag
        for i in range(num_palavras):
            value = bin_tag + words_add[i] + selector_bit
            cache[pointer][i+1] = value
        pointer += 1
        #Testing if pointer needs to return to its initial position
        if(pointer == num_linhas):
            pointer = 0


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