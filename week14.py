#1Drawing Book 

n = int(input())
p = int(input())

print (min(p//2, n//2 - p//2))


#2 Climbing the Leaderboard

scores_count = int(input())
scores = list(set(map(int, input().rstrip().split())))
alice_count = int(input())
alice = list(map(int, input().rstrip().split()))
scores.sort(reverse=True)
l=len(scores)
for a in alice:
  while l>0 and scores[l-1]<=a:
    l-=1
  print(l+1)



#3 Forming a Magic Square

s = [[int(i) for i in input().split(' ')] for j in range(3)]
n = [s[i][j] for i in range(3) for j in range(3)] 
tum_n = [[8,1,6,3,5,7,4,9,2],[6,1,8,7,5,3,2,9,4],[4,9,2,3,5,7,8,1,6],[2,9,4,7,5,3,6,1,8],[8,3,4,1,5,9,6,7,2],[4,3,8,9,5,1,2,7,6],[6,7,2,1,5,9,8,3,4],[2,7,6,9,5,1,4,3,8]]

toplam = []
for l in tum_n:
  toplam.append(sum([abs(n[i]-l[i]) for i in range(9)]))
print(min(toplam))




