from rest_framework.throttling import UserRateThrottle, AnonRateThrottle

class Our_throttle(AnonRateThrottle):
    scope = 'example'
