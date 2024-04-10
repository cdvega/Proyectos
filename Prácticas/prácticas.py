def flatten(iterable):

    def flatten_once(lista):
        output = []
        for element in lista:
            if isinstance(element, list):
                output.extend([x for x in element])
            else:
                output.append(element)

        if any(isinstance(x, list) for x in output):
            return flatten_once(output)
        else:
            return output

    return flatten_once(iterable)


print(flatten([1, [2, [3, [4]], 5], 6]))
