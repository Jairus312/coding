# program to find the amount of water that we can trap within a given set of bars

def findwater(a, a_size):

  # make array to hold the height of left tallest bar for any ith bar lefttallest = [0]*a_size 

  # make array to hold the height of the right tallest bar for any ith bar righttallest = [0]*a_size

  # initialize result
  water = 0

  # fill left array
  lefttallest[0] = a(0)
  for i in range( 1, a_size):
    lefttallest[i] = max(lefttallest[i-1], a[i])

  # fill right array
  righttallest[a_size-1] = a[a_size -1]
  for i in range(a_size -2, -1, -1):
    righttallest[i] = max(righttallest[i +1], a[i])

  # water trapped for any ith bar should be minium of the left and right highest bar - bar height
  for i in range(0, a_size):
    water += min(lefttallest[i], righttallest[i]) - a[i]
    
  return water 

a = [0,1,0,2,1,0,1,3,2,1,2,1]
bars = len(a)
print("water : ", findwater(a, bars))