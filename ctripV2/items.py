class list_entity:
    def __init__(self, hotelName, hotelId, star, cityName, positionArea):
        self.hotelName = hotelName
        self.hotelId = hotelId
        self.star = star
        self.cityName = cityName
        self.positionArea = positionArea


class review_entity:
    def __init__(self, score, totalReviews, keywords):
        self.score = score
        self.totalReviews = totalReviews
        self.keywords = keywords


class static_entity:
    def __init__(self, openDate, renovationDate, roomNum, hasDining, hasParking, hasWifi, hasPlane, description):
        self.openDate = openDate
        self.renovationDate = renovationDate
        self.roomNum = roomNum
        self.hasDining = hasDining
        self.hasParking = hasParking
        self.hasWifi = hasWifi
        self.hasPlane = hasPlane
        self.description = description


class place_entity:
    def __init__(self, placeName, stationName, stationDist):
        self.placeName = placeName
        self.stationName = stationName
        self.stationDist = stationDist


class room_entity:
    def __init__(self, name, baseRoomId, roomId, area, bed, bedType, floor, hasDinning, hasWindows, payType, promotion):
        self.name = name
        self.baseRoomId = baseRoomId
        self.roomId = roomId
        self.area = area
        self.bed = bed
        self.bedType = bedType
        self.floor = floor
        self.hasDinning = hasDinning
        self.hasWindows = hasWindows
        self.payType = payType
        self.promotion = promotion


class info_entity:
    def __init__(self, flight_distance, train_distance, subway_distance, place_info):
        self.flight_distance = flight_distance
        self.train_distance = train_distance
        self.subway_distance = subway_distance
        self.place_info = place_info


class brand_entity:
    def __init__(self, group_name, hotel_title, brand):
        self.group_name = group_name
        self.hotel_title = hotel_title
        self.brand = brand
