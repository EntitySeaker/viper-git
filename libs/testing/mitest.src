import_code("../functional.src")

testStack = []

ERROR_TYPES = {}
ERROR_TYPES.EXPECT = "expect"
ERROR_TYPES.TEST_PASS = "test_pass"
ERROR_TYPES.TEST_FAIL = "test_fail"

TestError = {}
TestError.type = null
TestError.message = null
TestError.New = function (type, message)
    err = new TestError
    err.type = type
    err.message = message
    return err
end function

addSpaceString = function (string, spaces)
    for i in range(0, spaces - 1)
        string = " " + string
    end for
    return string
end function

printErrors = function (errors, spaces = 0)
    for error in errors
        if error.type == ERROR_TYPES.EXPECT then
            print(addSpaceString(error.message, spaces))
        end if
        if error.type == ERROR_TYPES.TEST_PASS or error.type == ERROR_TYPES.TEST_FAIL then
            print(addSpaceString(error.message, spaces + 2))
            printErrors(error.errors, spaces + 4)
        end if
    end for
end function

handleFilterOnlyFailTests = function (error)
    if error.type == ERROR_TYPES.TEST_FAIL or error.type == ERROR_TYPES.EXPECT then
        return true
    end if
    return false
end function

test = function (name, callback)
    newTest = {
        "name": name,
        "callback": @callback,
        "errors": [],
        "tests": []
    }
    testStack.push(newTest)

    callback()

    testStack.pop()

    if filter(newTest.errors, @handleFilterOnlyFailTests).len > 0 and hasIndex(testStack, testStack.len - 1) then
        error = TestError.New(ERROR_TYPES.TEST_FAIL, "❌ " +  name)
        error.errors = newTest.errors
        testStack[testStack.len - 1].errors.push(error)
    else if hasIndex(testStack, testStack.len - 1) then
        pass = TestError.New(ERROR_TYPES.TEST_PASS, "✅ " +  name)
        pass.errors = newTest.errors
        testStack[testStack.len - 1].errors.push(pass)
    end if

    if testStack.len == 0 then
        if filter(newTest.errors, @handleFilterOnlyFailTests).len == 0 then
            print("✅ " + name)
        else
            print("❌ " + name)
        end if
        printErrors(newTest.errors, 2)
    end if
end function

expect = function (value)
    if testStack.len == 0 then
        print("expect must be called inside a test")
        return
    end if

    currentTest = testStack[testStack.len - 1]

    notFlag = false

    checks = {}
    checks.toBe = function (expected)
        if notFlag then
            if value == expected then
                currentTest.errors.push(TestError.New(ERROR_TYPES.EXPECT, value + " should not be " + expected))
            end if
        else
            if value != expected then
                currentTest.errors.push(TestError.New(ERROR_TYPES.EXPECT, value + " should be " + expected))
            end if
        end if
        return checks
    end function
    checks.setNot = function ()
        if notFlag == true then outer.notFlag = false
        if notFlag == false then outer.notFlag = true
        return checks
    end function
    checks.instanceOf = function (expected)
        if notFlag then
            if value isa expected then
                currentTest.errors.push(TestError.New(ERROR_TYPES.EXPECT, value + " should not be instance of " + expected))
            end if
        else
            if not(value isa expected) then
                currentTest.errors.push(TestError.New(ERROR_TYPES.EXPECT, value + " should be instance of " + expected))
            end if
        end if
        return checks
    end function
    checks.truthy = function ()
        if notFlag then
            if not(not(value)) == false then
                currentTest.errors.push(TestError.New(ERROR_TYPES.EXPECT, value + " should not be falsy"))
            end if
        else
            if not(not(value)) == true then
                currentTest.errors.push(TestError.New(ERROR_TYPES.EXPECT, value + " should be truthy"))
            end if
        end if
        return checks
    end function

    return checks
end function