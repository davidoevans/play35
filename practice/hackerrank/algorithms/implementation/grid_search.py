import re

def search_grid():
        result = ""
        for G_i in range(len(G)):
            for found in re.finditer(P[0], G[G_i]):
                start_column = found.start()
                start_row = G_i
                result = "YES"
                for P_i in range(1, len(P)):
                    if G[G_i + P_i].find(P[P_i]) == start_column:
                        result = "YES"
                    else:
                        result = "NO"
                        break
        return result


if __name__ == "__main__":

    t = int(input().strip())
    for a0 in range(t):
        R,C = input().strip().split(' ')
        R,C = [int(R),int(C)]
        G = []
        G_i = 0
        for G_i in range(R):
           G_t = str(input().strip())
           G.append(G_t)
        r,c = input().strip().split(' ')
        r,c = [int(r),int(c)]
        P = []
        P_i = 0
        for P_i in range(r):
           P_t = str(input().strip())
           P.append(P_t)

    print(search_grid(P, G))
