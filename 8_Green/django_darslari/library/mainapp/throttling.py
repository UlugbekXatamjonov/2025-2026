from rest_framework.throttling import AnonRateThrottle


class My_RateThrottle(AnonRateThrottle):
    scope = 'my_throttle'