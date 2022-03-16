def primes(n):
  is_prime = [True] * (n + 1)
  is_prime[0] = False
  is_prime[1] = False
  for i in range(2, int(n**0.5) + 1):
      if not is_prime[i]:
          continue
      for j in range(i * 2, n + 1, i):
          is_prime[j] = False
  return [i for i in range(n + 1) if is_prime[i]]

def main():
  l, r = map(int, input().split())
  if l == 1:
    print(r-l)
  else:
    maxPrime = primes(r)[-1]
    print(maxPrime-l)

main()
