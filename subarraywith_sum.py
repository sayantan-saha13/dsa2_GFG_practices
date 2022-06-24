def subarraySum(self,arr,n,sum):
      for i in range(n):
        current_sum=arr[i]
        j=i+1
        while j<=n:
            if current_sum==sum:
                print("sum found in between",i,j-1)
                return
            if current_sum>sum or j==n:
                break
            current_sum=current_sum+arr[j]
            j+=1
arr=[1,2,3,7,5]
n=len(arr)

