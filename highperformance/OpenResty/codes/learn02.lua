
local set = {1, 2, 3}
local set2 = {2, 3, 4}

local union = function(self, set)
    local result = {}
    local temp = {}
    for i, v in ipairs(self) do temp[v] = true end
    for i, v in ipairs(set) do temp[v] = true end

    for k, v in pairs(temp) do
        table.insert(result, k)
        --result[#result + 1] = k
    end
    return result
end

setmetatable(set, { __add = union})


local set3 = set + set2

for i, v in ipairs(set3) do
    print(i, v)
end

print(getmetatable(set))

local user = require('user')

me = user:new('silence')
print(me:get_name())
me:set_name('kk')
print(me:get_name())
