def wrapper(f):
    def fun(l):
        # complete the function
        phonenumber = ["+91 " + nums[-10:-5] + " "+nums[-5:] for nums in l]
        f(phonenumber)
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 
