def read_file(filename):
    with open(filename,'r',encoding = "utf-8") as fr:
        score_ls = []
        for line in fr:
            score_ls.append(line.strip().split(','))
    return score_ls

def total(score_ls):
    total_score = []
    score_ls[0].append('total')
    for lst in score_ls[1:]:
        total_score.append(lst + [str(sum(map(int,lst[1:])))])
    return [score_ls[0]] + total_score
def sort_list(score_total,n):
    title_ls = [score_total[0]]
    score_ls = score_total[1:]
    score_ls.sort(key = lambda x:int(x[n]),reverse = True )
    score_sort = title_ls + score_ls
    return score_sort
def write_file(score_sort,new_file):
    with open(new_file,'w',encoding='utf-8') as fw:
        for x in score_sort:
            fw.write(','.join(x) + '\n')
    print("finished")

if __name__ == '__main__':
    file = 'score.csv'
    score = read_file(file)
    score_total = total(score)
    print(score_total)
    score_sorted = sort_list(score_total,5)
    write_file(score_sorted,'score_sorted.csv')
    
#print(total(read_file("score.csv")))