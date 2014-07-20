require 'open-uri'

data = open("http://www.codingexcuses.com", "Accept" => "text/plain")

puts data.read