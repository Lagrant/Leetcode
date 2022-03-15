"""
def find_pairs_with_given_difference(arr, k):
  # pass # your code goes here
  d_arr = {}
  for i in range(len(arr)):
    d_arr[arr[i]] = i
    
  ans = []
  for i in range(len(arr)):
    if (arr[i] + k in d_arr):
      ans.append([arr[i] + k, arr[i]])
  
  return ans
"""

def find_pairs_with_given_difference(arr, k):
  output = []
  #key = x - y
  #value = num
  pairs = {}
  
  #num - k = y
  #create map of differnce and num 
  for num in arr:
    pairs[num - k] = num
  
  #y = num - k
  #use key to find the pair
  for num in arr:
    if num in pairs:
      output.append([pairs[num], num])
  
  return output 




"""
O(N^2)

for i in arr:
  for j in arr:
    if arr[i] - arr[j] == k:
    ans.append([i, j])

d_arr = {value of the array : index of the array}

for i in arr:
  d_arr[arr[i]] = i

k = 1
d_arr = {0:0, -1:1, -2:2, 2:3, 1:4}
        a[i] == 0, a[i] - k == -1 => -1 in d_arr => [[0, -1]]
              a[i] == -1 a[i] - k == -2 => -2 in d_arr => [[0, -1],[-1, -2]]
                    a[i] == -2, a[i] - k == -3 => not in d_arr
                          a[i] == 2, a[i] - k == 1 => in d_arr => [[0, -1],[-1, -2],[2, 1]]
                                a[i] == 1, a[i] - k == 0 => in d_arr => [[0, -1],[-1, -2],[2, 1], [1,0]]
        0=>1=>in=>[[1,0]]
              -1=>0=>in=>[[1,0], [0, -1]]
                    -2
 

x - y == k
# y == x - k
x = y + k

for i in arr:
  if (arr[i] + k in d_arr):
    ans.append([arr[i] + k, arr[i]])

O(N)
O(N) for space
"""


#ascii range 97-126
#convert to ascii ord()
#convert back int number chr()
def decrypt(word):
  
  
 # pass # your code goes here
  lower = 97  # ascii
  upper = 122
  
  res = [] # stores descrypted str
  if (word[0] == 'a'):  # inital char[0]
    res.append('z')
  else:
    res.append(ord(chr(word[0]) - 1))

  nums = [chr[res[0]]]
  for i in range(len(word)):
    nums.append(chr(word[i]))

  sec_nums = [nums[-1]]
  for i in range(1, len(nums)):
    layer2 = sec_nums[i - 1] + sec_nums[i - 2]
    diff = nums[i] - sec_nums[i - 1]
    # l_bound = (low - diff) / 26
    times = (upper - diff) // 26
    nums.append(26 * times + diff)
    
    
    '''
    Step 1:	99	114	105	109	101
    214
    
    Step 2:	100	214	319	428	529
    
    Step 3:	100	110	111	116	113
    outpu = [100,110]
    '''
    
    ascValue = []
    for i in word:
      ascValue.append(ord(i))
      
    #100 110 111 116 113
    
    result = [99,114]
    secArr = [100,214]
    
    i =2    
    for i in range(1,len(ascValue)):
      curr = ascValue[i]
      curr -= secArr[i-1] #-5
      updated = getInRange(curr)
      result.append(curr)
      secArr.append(curr + secArr[i-1])
    

    
def getInRange(curr):
  while curr < 97:
    curr +=26
  return curr
"""

c r i m e

100 110 111 116 113

if word[0] != 'z' no need to subtract 26

num [100 110 111 116 113]

word[0] == chr(num[0] - 1)


real[1] = num[1] + 26 * k1 - (num[0])
real[2] = num[2] + 26 * k2 - real[1]
real[3] = num[3] + 26 * k3 - real[2]
...

word[0] == z
num of z 122 + 1= 123 - 26 = 97


110 -100 = 10 +26 97 
111- 214 = -5 +26

num [100 110 111 116 113]
secondArray = [100,214]
output = [99,114]
for i in range(1, lenNUm):
    10 114
  
  
"""