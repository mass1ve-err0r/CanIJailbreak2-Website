# Minimum Version List
MinVersionMap = {
    "iPhone 2G": "1.0",
    "iPhone 3G": "2.0", "iPhone 3GS": "3.0",
    "iPhone 4": "4.0", "iPhone 4S": "5.0",
    "iPhone 5": "6.0", "iPhone 5C": "7.0", "iPhone 5S": "7.0",
    "iPhone 6": "8.0", "iPhone 6 Plus": "8.0",
    "iPhone 6S": "9.0", "iPhone 6S Plus": "9.0",
    "iPhone 7": "10.0", "iPhone 7 Plus": "10.0",
    "iPhone 8": "11.0", "iPhone 8 Plus": "11.0", "iPhone X": "11.1",
    "iPhone XS": "12.0", "iPhone XS Max": "12.0", "iPhone XR": "12.0",
    "iPhone 11": "13.0", "iPhone 11 Pro": "13.0", "iPhone 11 Pro Max": "13.0",
    "iPhone SE 1": "9.3", "iPhone SE 2": "13.4.1",
    "iPhone 12": "14.1", "iPhone 12 Mini": "14.1", "iPhone 12 Pro": "14.1", "iPhone 12 Pro Max": "14.1",
    "iPad 1": "3.2", "iPad 2": "4.3", "iPad 3": "5.1", "iPad 4": "6.0", "iPad 5": "10.2.1", "iPad 6": "11.3", "iPad 7": "13.1", "iPad 8": "14",
    "iPad Air 1": "7.0.3", "iPad Air 2": "8.1", "iPad Air 3": "12.2", "iPad Air 4": "14.0",
    "iPad Mini 1": "6.0.1", "iPad Mini 2": "7.0.3", "iPad Mini 3": "8.1", "iPad Mini 4": "9.0", "iPad Mini 5": "12.2",
    "iPad Pro 12.9 1": "9.1", "iPad Pro 9.7": "9.3", "iPad Pro 12.9 2": "10.3.2", "iPad Pro 10.5": "10.3.2", "iPad Pro 11 1": "12.1", "iPad Pro 12.9 3": "12.1", "iPad Pro 11 2": "13.4", "iPad Pro 12.9 4": "13.4", "iPad Pro 11 3": "14.4", "iPad Pro 12.9 5": "14.4",
    "iPod Touch 1": "1.1", "iPod Touch 2": "2.1.1", "iPod Touch 3": "3.1.1", "iPod Touch 4": "4.1", "iPod Touch 5": "6.0", "iPod Touch 6": "8.4", "iPod Touch 7": "12.3.1"
}

# Maximum Version List
GMaxiOS = "14.5"
MaxVersionMap = {
    "iPhone 2G": "3.1.3",
    "iPhone 3G": "4.2.1", "iPhone 3GS": "6.1.6",
    "iPhone 4": "7.1.2", "iPhone 4S": "9.3.6",
    "iPhone 5": "10.3.4", "iPhone 5C": "10.3.3", "iPhone 5S": "12.5.1",
    "iPhone 6": "12.5.1", "iPhone 6 Plus": "12.5.1",
    "iPhone 6S": GMaxiOS, "iPhone 6S Plus": GMaxiOS,
    "iPhone 7": GMaxiOS, "iPhone 7 Plus": GMaxiOS,
    "iPhone 8": GMaxiOS, "iPhone 8 Plus": GMaxiOS, "iPhone X": GMaxiOS,
    "iPhone XS": GMaxiOS, "iPhone XS Max": GMaxiOS, "iPhone XR": GMaxiOS,
    "iPhone 11": GMaxiOS, "iPhone 11 Pro": GMaxiOS, "iPhone 11 Pro Max": GMaxiOS,
    "iPhone SE 1": GMaxiOS, "iPhone SE 2": GMaxiOS,
    "iPhone 12": GMaxiOS, "iPhone 12 Mini": GMaxiOS, "iPhone 12 Pro": GMaxiOS, "iPhone 12 Pro Max": GMaxiOS,
    "iPad 1": "5.1.1", "iPad 2": "9.3.6", "iPad 3": "9.3.6", "iPad 4": "10.3.4", "iPad 5": GMaxiOS, "iPad 6": GMaxiOS, "iPad 7": GMaxiOS, "iPad 8": GMaxiOS,
    "iPad Air 1": "12.5.1", "iPad Air 2": GMaxiOS, "iPad Air 3": GMaxiOS, "iPad Air 4": GMaxiOS,
    "iPad Mini 1": "9.3.6", "iPad Mini 2": "12.5.1", "iPad Mini 3": "12.5.1", "iPad Mini 4": GMaxiOS, "iPad Mini 5": GMaxiOS,
    "iPad Pro 12.9 1": GMaxiOS, "iPad Pro 9.7": GMaxiOS, "iPad Pro 12.9 2": GMaxiOS, "iPad Pro 10.5": GMaxiOS, "iPad Pro 11 1": GMaxiOS, "iPad Pro 12.9 3": GMaxiOS, "iPad Pro 11 2": GMaxiOS, "iPad Pro 12.9 4": GMaxiOS, "iPad Pro 11 3": GMaxiOS, "iPad Pro 12.9 5": GMaxiOS,
    "iPod Touch 1": "3.1.3", "iPod Touch 2": "4.2.1", "iPod Touch 3": "5.1.1", "iPod Touch 4": "6.1.6", "iPod Touch 5": "9.3.5", "iPod Touch 6": "12.5.1", "iPod Touch 7": GMaxiOS
}

# Mappings of Processor Generations (with some exceptions such as iP8 & X)
DeviceMapPGNamed = {
    '2G': ['iPhone 2G'],
    '3G': ['iPhone 3G', 'iPod Touch 1', 'iPod Touch 2'],
    '3GS': ['iPhone 3GS', 'iPod Touch 3'],
    '4': ['iPhone 4', 'iPad 1', 'iPod Touch 4'],
    '4S': ['iPhone 4S', 'iPad 2', 'iPad 3', 'iPad Mini 1', 'iPod Touch 5'],
    '5': ['iPhone 5', 'iPhone 5C', 'iPad 4'],
    '5S': ['iPhone 5S', 'iPad Air 1', 'iPad Mini 2', 'iPad Mini 3'],
    '6': ['iPhone 6', 'iPhone 6 Plus', 'iPad Air 2', 'iPad Mini 4', 'iPod Touch 6'],
    '6S': ['iPhone 6S', 'iPhone 6S Plus', 'iPhone SE 1', 'iPad 5', 'iPad Pro 12.9 1', 'iPad Pro 9.7'],
    '7': ['iPhone 7', 'iPhone 7 Plus', 'iPad 6', 'iPad 7', 'iPad Pro 12.9 2', 'iPad Pro 10.5', 'iPod Touch 7'],
    '8': ['iPhone 8', 'iPhone 8 Plus'],
    'X': ['iPhone X'],
    'XS': ['iPhone XR', 'iPhone XS', 'iPhone XS Max', 'iPad 8', 'iPad Air 3', 'iPad Pro 11 1', 'iPad Pro 12.9 3', 'iPad Pro 11 2', 'iPad Pro 12.9 4', 'iPad Mini 5'],
    '11': ['iPhone 11', 'iPhone 11 Pro', 'iPhone 11 Pro Max', 'iPhone SE 2'],
    '12': ['iPhone 12 Mini', 'iPhone 12', 'iPhone 12 Pro', 'iPhone 12 Pro Max', 'iPad Air 4'],
    'M1': ['iPad Pro 11 3', 'iPad Pro 12.9 5']
}

# List DeviceProcessors in chronological order
DeviceMapPG = ["2G", "3G", "3GS", "4", "4S", "5", "5S", "6", "6S", "7", "8", "X", "XS", "11", "12", "M1"]
