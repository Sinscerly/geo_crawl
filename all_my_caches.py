import cacheInfo

def main():
    f = open("../my_caches.txt", "r")
    for x in f:
        cache_details(x.rstrip('\n'))

def cache_details(code):
    c = cacheInfo.cacheInfo(code)
    print("---------------------------------------------")
    print("\t" + c.geoCode.upper() + ": " + c.get_name())
    print("---------------------------------------------")
    print("Placed on: \t" + c.get_datePlaced() + " that's " + str(c.get_daysOld()) + " days ago")
    print("Last find: \t" + c.get_lastFind() + " that's " + str(c.get_dayslastFind()) + " days ago")
    print("Total finds: \t" + str(c.get_finds()))
    print("Finds a day: \t" + str(round(c.get_finds() / c.get_daysOld(), 2)))
    print("Didn't finds: \t" + str(c.get_doNotFinds()))


if __name__ == "__main__":
    main()

