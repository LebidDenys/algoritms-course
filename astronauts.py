def journeyToMoon(astronauts, pairs):
    countries = []
    country_astronauts = 0
    for (as_one, as_two) in pairs:
        was_added = False
        for country in countries:
            if as_one in country:
                country.append(as_two)
                was_added = True
                country_astronauts = country_astronauts + 1
                break
            if as_two in country:
                country.append(as_one)
                was_added = True
                country_astronauts = country_astronauts + 1
                break
        if not was_added:
            countries.append([as_one, as_two])
            country_astronauts = country_astronauts + 2
    for _ in range(astronauts - country_astronauts):
        countries.append([1])
    result = 0
    for country in countries:
        for countryy in countries:
            if countryy is country:
                continue
            else:
                result = result + len(country) * len(countryy)
        countries.remove(country)
    return result


(astro, pairs_n) = map(int, input().strip().split())
pairs_arr = []
for _ in range(pairs_n):
    pairs_arr.append(list(map(int, input().strip().split())))

print(solution(astro, pairs_arr))
