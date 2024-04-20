test "map", function()
    a = [1, 2, 3]
    b = map(a, function (x)
        return x * 2
    end function)

    expect(b).toBe([2, 4, 6])
end function

test "filter", function()
    a = [1, 2, 3, 4, 5, 6]
    b = filter(a, function (x)
        return x % 2 == 0
    end function)

    expect(b).toBe([2, 4, 6])
end function

test "reduce", function()
    test "reduce without initial value", function()
        a = [1, 2, 3, 4, 5, 6]
        b = reduce(a, function (x, y)
            return x + y
        end function)

        expect(b).toBe(21)
    end function

    test "reduce with initial value", function()
        a = [1, 2, 3, 4, 5, 6]
        b = reduce(a, function (x, y)
            return x + y
        end function, 10)

        expect(b).toBe(31)
    end function
end function

test "find", function()
    a = [1, 2, 3, 4, 5, 6]
    b = find(a, function (x)
        return x == 3
    end function)

    expect(b).toBe(3)

    b = find(a, function (x)
        return x == 7
    end function)

    expect(b).toBe(null)
end function

test "every", function()
    a = [1, 2, 3, 4, 5, 6]
    b = every(a, function (x)
        return x < 7
    end function)

    expect(b).toBe(true)

    b = every(a, function (x)
        return x < 6
    end function)

    expect(b).toBe(false)
end function

test "flat", function()
    a = [1, 2, 3, [4, 5, 6]]
    b = flat(a)

    expect(b).toBe([1, 2, 3, 4, 5, 6])
end function

test "distinct", function()
    a = [1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5]
    b = distinct(a)

    expect(b).toBe([1, 2, 3, 4, 5, 6])
end function