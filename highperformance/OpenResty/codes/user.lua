_M = {}
_M.VERSION = 1.0

local mt = { __index = _M }

_M.new = function(self, name)
    return setmetatable({name = name}, mt)
end

_M.get_name = function(self)
    return self.name
end

_M.set_name = function(self, name)
    self.name = name
end

return _M
