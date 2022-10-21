from math import sqrt
import random

vector1 = [3, 8, 9, 10, 12]
vector2 = [8, 7, 7, 5, 6]


def vec_sum(v1, v2):
    v3 = []
    for i in range(len(v1)):
        v3.append(v1[i] + v2[i])
    return v3


print(vec_sum(vector1, vector2))


def scal_prod(v1, v2):
    sum = 0
    for i in range(len(v1)):
        sum += (v1[i] * v2[i])
    return sum


print(scal_prod(vector1, vector2))


def rand_vec(length):
    vector = []
    for i in range(length):
        vector.append(random.randint(1, 100))
    return vector


def vec_avg(vec):
    return sum(vec) / len(vec)


def stand_dev(vec):
    return sqrt(sum(list(map(lambda num: pow(num - vec_avg(vec), 2), vec))) / len(vec))


def vec_norm(vec):
    new_vec = []
    for i in range(len(vec)):
        new_vec.append((vec[i] - min(vec)) / (max(vec) - min(vec)))
        if vec[i] == max(vec): print('MAX: ' + str(vec[i]) + ", old position: " + str(i) + ", new value: " + str(new_vec[i]))
    return new_vec


def vec_stand(vec):
    new_vec = list(map(lambda num: (num - vec_avg(vec)) / stand_dev(vec), vec))
    print("AVG: " + str(vec_avg(new_vec)))
    print("STD DEVIATION: " + str(stand_dev(new_vec)))
    return new_vec


print("\n RANDOM VECTOR")
RAND_VEC = rand_vec(50)
print(RAND_VEC)

print("\nVECTOR AVG")
print(vec_avg(RAND_VEC))

print("\nMAX AND MIN")
print([max(RAND_VEC), min(RAND_VEC)])

print("\nSTANDARD DEVIATION")
print(stand_dev(RAND_VEC))

print("\nVECTOR NORMALISATION")
print(vec_norm(RAND_VEC))

print("\nVECTOR STANDARDISATION")
print(vec_stand(RAND_VEC))


