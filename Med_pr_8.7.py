#Task number three
print(*sorted((set(int(ind) for ind in input().split())  & set(int(ind) for ind in input().split()) ) - set(int(ind) for ind in input().split()) , reverse=True))