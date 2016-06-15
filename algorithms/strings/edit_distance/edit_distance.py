'''
    type: algorithm
    theme: string
    sub-theme: dynamic programming
    name: edit distance
    author of code: Evgeny @missingdays Bovykin

'''

def edit_distance(s1, s2):
    """
    Calculates edit distance of two strings using dynamic programming

    Edit distance is a way to describe how two strings are similar
    Formally, edit distance of s1 and s2 is how much operations it takes to convert s1 to s2
    Allowed operations are
        - add new character to any position
        - remove any character
        - replace character


    Time: O(m*n)
    Space: O(m*n)
    where n = len(s1), m = len(s2)

    or in general

    Time: O(n^2)
    Space: O(n^2)
    where n is max(len(s1), len(s2))
    """
    distance = []

    for i in range(len(s1) + 1):

        column = [None] * (len(s2) + 1)

        distance.append(column)

    # Init values
    # to edit None to string it requires
    # len(string) operations
    for i in range(len(s1) + 1):

        distance[i][0] = i

    for i in range(len(s2) + 1):

        distance[0][i] = i

    for i in range(1, len(s1) + 1):
        for k in range(1, len(s2) + 1):

            # If characters in this string are the same
            # we can either add one character to s1 (1 op)
            # or add one character to s2 (1 op)
            # or don't touch them (0 op)
            if s1[i-1] == s2[k-1]:

                distance[i][k] = min(
                    distance[i-1][k] + 1,
                    distance[i][k-1] + 1,
                    distance[i-1][k-1]
                )
            # If characters in this string are not the same
            # we can either add one character to s1 (1 op)
            # or add one character to s2 (1 op)
            # or change one character to another (1 op)
            else :

                distance[i][k] = min(
                    distance[i-1][k] + 1,
                    distance[i][k-1] + 1,
                    distance[i-1][k-1] + 1
                )

    return distance[len(s1)][len(s2)]
