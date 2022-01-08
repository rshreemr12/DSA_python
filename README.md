# DSA_python
Analyse different datastructres and algorithms in python with their complexity

Use cases: Why do we need complex datastructres and where do we use them usually?

Lets say we need to develop a website with millions of users and to load each user's specific profile it consumes 10 sec roughly.
10 Secs is occupied by 1 core. Even if we implement in the best possible way using multi process enviroment,
in order to serve 100 users we will end up freezing all cores for 100*10  secs.  
Lets say we have 32 Gb Ram with octa core machine. Put to together all 8 cores serving the request we can serve 80 request in 10sec.

User experience will be pretty bad if it takes 10s just to load up the landing page
With latest possible techniques of cloud (AWS or Azure). Even with scaling it with more cores and Ram we will end up costing more money
while we could use techniques for better CRUD. 

#### Linear Search :
if we want to search any element in the given list, we try to compare the target number with the rest of elements.
`nums = [9,8,7,6,5,4,3,2,1]`

if the target is 6
we end up doing 4 iterations 

lets consider worst case scenario.
target = 1
number of iterations needed is 9 which is len(nums)
For any given list finding a element uisng linear search is O(N) making its time complexity
space consumed to check the target number is O(1)


