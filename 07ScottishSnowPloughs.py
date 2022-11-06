snow_ploughs = {'driver100': 'BFG Big Friendly Gritter',
                'driver1': 'For Your Ice Only',
                'driver2': 'Gritallica',
                'driver3': 'Gritter Thunberg',
                'driver4': 'Grit Expectations',
                'driver5': 'Gritty Gritty Bang Bang',
                'driver6': 'License to Chill',
                'driver7': 'Luke Snowwalker',
                'driver8': 'Nitty Gritty',
                'driver9': 'Yes Sir, Ice Can Boogie',
                'driver10': 'Spready Mercury',
                'driver11': 'Snowkemon Go',
                'driver12': 'Slippy McGritty',
                'driver13': 'Gritty McGritface',
                'driver14': 'Sir Grits-A-Lot',
                'driver15': 'Sir Andy Flurry',
                'driver16': "Plougher O'Scotland"}


def implement_changes(snow_ploughs):
    """
    Implement changes according to assignment rules
    :return: amended dictionary
    """
    # driver14 no longer has a snow plough assigned
    # I had used ''. Were meant to use None
    snow_ploughs['driver14'] = None

    # change the name of the driver15
    snow_ploughs['driver15'] = 'Ice Ice Baby'

    # driver 16 is leaving the company and new user,
    # driver17 will be assigned his snow plough
    snow_ploughs['driver17'] = snow_ploughs['driver16']
    del snow_ploughs['driver16']

    # driver4, driver5 and driver6 are leaving at the same time,
    # but their snow plough names are to be stored in a list
    # called unallocated. Use pop in a loop.
    unallocated = []
    leavers = ['driver4', 'driver5', 'driver6']
    for user in range(len(leavers)):
        unallocated.append(snow_ploughs.pop(leavers[user]))
    '''
    Solution used in the example:
    for driver in ('driver4', 'driver5', 'driver6'):
    	    unallocated += [snow_ploughs.pop(driver)]
    '''

    # driver8 gets another machine
    # make the entity list first
    snow_ploughs['driver8'] = [snow_ploughs['driver8'], 'kodiak']
    # after it's become a list can use list append function
    # snow_ploughs['driver8'].append('string')

    # print a list of drivers with their machine in any order
    # print each driver/snow plough pair on a separate line
    for driver in sorted(snow_ploughs.items()):
        print(driver)

    # print a list of unallocated machines, sorted alphabetically
    print('\nUnallocated machines: ', sorted(unallocated))

    return 'The end.'


print(implement_changes(snow_ploughs))