from Crypto.Random.random import randrange
from machine import Machine
from assembly import assembly # add line on 24/04 by JBB

def Fib(n):
    if n < 2:
        return n
    A = 0
    B = 1
    for _ in range(n - 1):
        C = A + B
        A = B
        B = C
    return B

def correctness(code):
    for _ in range(64):
        a = randrange(1024)
        c = Machine(code, a)  
        c.runCode()
        
        if c.error:
            print("[!] Error!")
            exit()

        if c.R0 != Fib(a):
            print("[!] Nope, you did not implement Fibonacci")
            exit()
    
    flag = open("flag.txt").read().strip()
    print(f"[+] Congrats! Here is the flag: {flag}")

if __name__ == "__main__":

    print("Enter your bytecode in hexadecimal:")
    #try:
    print("Enter your ASM instructions")
    asm = [
           #;----- HEAD -----
         "MOV R7, #2",    
         "CMP R5, R7",    
     "JNCA begin",   
         "MOV R6, #1",    
         "MOV R0, #1",    
         "XOR R1, R1, R1",
         "XOR R2, R2, R2",
          #;--- FIBONACCI --
     "fibo:",            
         "SUB R5, R5, R6",
         "CMP R5, R6",    
         "JNCA exit",     
         "MOV R2, R0",   
         "ADD R0, R0, R1",
         "MOV R1, R2",    
         "JA fibo",       
          #;-CASE OF 0 AND 1
     "begin:",           
         "MOV R0, R5",          
          #;----- EXIT -----",
     "exit:",
         "STP"
        ]
    code = assembly(asm)
    print(code)
    correctness(code)
   # except:
    print("Please check your inputs.")
