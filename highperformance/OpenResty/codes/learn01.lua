print('hello, slience')

print(type(1))
print(type(0.1))

print(type(false))
print(type(true))

print(type(nil))

print(type(print))
print(type(type))

local name = 'kk'
local age

print(name)
print(age)

if true then
    print('true is true')
else
    print('true is false')
end

if false then
    print('false is true')
else
    print('false is false')
end


if nil then
    print('nil is true')
else
    print('nil is false')
end

if '' then
    print('"" is true')
else
    print('"" is false')
end

if 0 then
    print('0 is true')
else
    print('0 is false')
end

local map = {
    blog = 'http://imsilence.github.io/',
    qq = '782874382',
    age = 29,
    ['name'] = 'silence',
    [10] = 168,
    146,
    ['user'] = {"kk", "silence"}
}

print(map[1])
print(map['blog'])
print(map[10])
print(map.qq)
print(map.user[1])
print(map.user[2])

local add = function(a, b)
    return a + b
end

print(add(1, 2))

print(1 + 2)
print(1 - 2)
print(1 * 2)
print(1 / 2)
print(1 % 2)
print(3 ^ 2)

print(1 > 2)
print(1 >= 2)
print(1 < 2)
print(1 <= 2)
print(1 == 2)
print(1 ~= 2)

print('a' > 'b')
print('a' == 'b')
print('a' ~= 'b')

print(true and true)
print(true and false)
print('silence' and nil)
print('silence' and 'kk')

print(false or false)
print(true or false)
print(nil or 'silence')
print('silence' or 'kk')

print('my name is'..' '..'silence')
print(string.format('name: %s, age: %d, height: %.2f', 'silence', 29, 168.3))
print(table.concat({1, 2, '3'}))


local score = 70
if score > 90 then
    print('> 90')
elseif score > 60 then
    print('> 60')
else
    print('< 60')
end

local idx = 0
local sum = 0
while idx < 10 do
    sum = sum + idx
    idx = idx + 1
end
print(sum)

local idx = 0
local sum = 0
while true do
    sum = sum + idx
    idx = idx + 1
    if idx >= 10 then
        break
    end
end
print(sum)

local idx = 0
local sum = 0
repeat
    sum = sum + idx
    idx = idx + 1
until idx >= 10
print(sum)

local sum = 0
for idx = 1, 9 do
    sum = sum + idx
end
print(sum)

local sum = 0
for idx = 1, 9, 2 do
    sum = sum + idx
end
print(sum)

local scores = {1, 2, 3, 4, 5}
for key, value in ipairs(scores) do
    print(string.format('index:%s, value:%s', key, value))
end

local scores = {['kk'] = 1, ['silence'] = 2}
for key, value in pairs(scores) do
    print(string.format('key:%s, value:%s', key, value))
end

local selfprint = function(a, b)
    print(a, b)
end

print(selfprint(1, 2, 3))
print(selfprint(1))

local change = function(a, b)
    if a > b then
        local tmp = a
        a = b
        b = tmp
        print(a, b)
    end
end

local a = 2
local b = 1
print(a, b)
change(a, b)
print(a, b)

local change_args = function(args)
    if args.a > args.b then
        local tmp = args.a
        args.a = args.b
        args.b = tmp
        print(args.a, args.b)
    end
end

local args = {a = 2, b = 1}
change_args(args)
print(args.a, args.b)

local print_args = function(...)
    print(table.concat({...}, ' '))
end

print_args(1, 2, 3)

local init_args = function()
    return 1, 2
end

local a = init_args()
print(a)
local a, b, c = init_args()
print(a, b, c)


local callbacks = {}
callbacks.print = function(...) print(...) end

local action = function(callback, ...)
    callbacks[callback](unpack({...}))
end

action('print', 1, 2, 3)

local utils = require('utils')
utils.print(1, 2, 3)


local name = 'silence'
print(string.byte(name, 1, 10))
print(string.char(11, 12))
print(string.upper('aA'))
print(string.lower('aA'))
print(string.len('a12'))

local file = io.input('utils.lua')

while true do
    local line = io.read()
    if nil == line then
        break
    end
    print(line)
end

io.close()

local file = io.open('log.txt', 'ab+')
io.output(file)
io.write(string.format('%s\n', os.time()))
io.close(file)

local file = io.open('utils.lua', 'r')
for line in file:lines() do
    print(line)
end
file:close()


local file = io.open('log.txt', 'ab+')
file:write(string.format('%s\n', os.time()))
file:close()
