i = 0
    selected.append(arr[i])
 
    for j in range(1, n):
       
      '''If this activity has start time greater than or
         equal to the finish time of previously selected
         activity, then select it'''
      if arr[j][0] >= arr[i][1]:
          selected.append(arr[j])
          i = j
    return selected
 
