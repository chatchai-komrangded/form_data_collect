import json
import os
import pytest
from pytest_mock import mocker

import boto3 

from src.database_stream import app

@pytest.fixture()
def ddb_event():
    """ Generates API GW Event"""

    return {
        "Records": [
            {
            "eventID": "fd797f3039d18236c943d07637301e36",
            "eventName": "INSERT",
            "eventVersion": "1.1",
            "eventSource": "aws:dynamodb",
            "awsRegion": "eu-central-1",
            "dynamodb": {
                "ApproximateCreationDateTime": 1603714567.0,
                "Keys": {
                "sk": {
                    "S": "sebastien.stormacq@gmail.com"
                },
                "pk": {
                    "S": "nata.coach.landing_page"
                }
                },
                "NewImage": {
                "name": {
                    "S": "stormacq"
                },
                "sk": {
                    "S": "sebastien.stormacq@gmail.com"
                },
                "created_at": {
                    "N": "1603709167"
                },
                "pk": {
                    "S": "nata.coach.landing_page"
                },
                "event": {
                    "M": {
                    "headers": {
                        "M": {
                        "content-length": {
                            "S": "86"
                        },
                        "referer": {
                            "S": "https://nata.coach/landing/"
                        },
                        "accept-language": {
                            "S": "en-US,en;q=0.8,fr-FR;q=0.5,fr;q=0.3"
                        },
                        "x-forwarded-proto": {
                            "S": "https"
                        },
                        "origin": {
                            "S": "https://nata.coach"
                        },
                        "x-forwarded-port": {
                            "S": "443"
                        },
                        "x-forwarded-for": {
                            "S": "54.239.6.177"
                        },
                        "accept": {
                            "S": "text/html, */*; q=0.01"
                        },
                        "x-amzn-trace-id": {
                            "S": "Root=1-5f96a8ee-6da99b0d095f29287022aa30"
                        },
                        "host": {
                            "S": "vija6eqvi4.execute-api.eu-central-1.amazonaws.com"
                        },
                        "content-type": {
                            "S": "application/x-www-form-urlencoded; charset=UTF-8"
                        },
                        "accept-encoding": {
                            "S": "gzip, deflate, br"
                        },
                        "user-agent": {
                            "S": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:82.0) Gecko/20100101 Firefox/82.0"
                        }
                        }
                    },
                    "isBase64Encoded": {
                        "BOOL": True
                    },
                    "rawPath": {
                        "S": "/prod/form"
                    },
                    "requestContext": {
                        "M": {
                        "accountId": {
                            "S": "401955065246"
                        },
                        "timeEpoch": {
                            "N": "1603709166956"
                        },
                        "routeKey": {
                            "S": "POST /form"
                        },
                        "stage": {
                            "S": "prod"
                        },
                        "domainPrefix": {
                            "S": "vija6eqvi4"
                        },
                        "requestId": {
                            "S": "VA9VWhZHliAEJCA="
                        },
                        "domainName": {
                            "S": "vija6eqvi4.execute-api.eu-central-1.amazonaws.com"
                        },
                        "http": {
                            "M": {
                            "path": {
                                "S": "/prod/form"
                            },
                            "protocol": {
                                "S": "HTTP/1.1"
                            },
                            "method": {
                                "S": "POST"
                            },
                            "sourceIp": {
                                "S": "54.239.6.177"
                            },
                            "userAgent": {
                                "S": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:82.0) Gecko/20100101 Firefox/82.0"
                            }
                            }
                        },
                        "time": {
                            "S": "26/Oct/2020:10:46:06 +0000"
                        },
                        "apiId": {
                            "S": "vija6eqvi4"
                        }
                        }
                    },
                    "routeKey": {
                        "S": "POST /form"
                    },
                    "body": {
                        "S": "cGs9bmF0YS5jb2FjaC5sYW5kaW5nX3BhZ2Umc2s9ZW1haWwmbmFtZT1zdG9ybWFjcSZlbWFpbD1zZWJhc3RpZW4uc3Rvcm1hY3ElNDBnbWFpbC5jb20="
                    },
                    "rawQueryString": {
                        "S": ""
                    },
                    "version": {
                        "S": "2.0"
                    }
                    }
                },
                "email": {
                    "S": "sebastien.stormacq@gmail.com"
                }
                },
                "SequenceNumber": "3133900000000004608185093",
                "SizeBytes": 1323,
                "StreamViewType": "NEW_IMAGE"
            },
            "eventSourceARN": "arn:aws:dynamodb:eu-central-1:401955065246:table/nata-data-collection-form/stream/2020-10-26T12:09:18.744"
            }
        ]
        }

@pytest.fixture()
def ddb_event_multiple():
    return {
        "Records": [
            {
            "eventID": "fd797f3039d18236c943d07637301e36",
            "eventName": "INSERT",
            "eventVersion": "1.1",
            "eventSource": "aws:dynamodb",
            "awsRegion": "eu-central-1",
            "dynamodb": {
                "ApproximateCreationDateTime": 1603714567.0,
                "Keys": {
                "sk": {
                    "S": "sebastien.stormacq@gmail.com"
                },
                "pk": {
                    "S": "nata.coach.landing_page"
                }
                },
                "NewImage": {
                "name": {
                    "S": "stormacq"
                },
                "sk": {
                    "S": "sebastien.stormacq@gmail.com"
                },
                "created_at": {
                    "N": "1603709167"
                },
                "pk": {
                    "S": "nata.coach.landing_page"
                },
                "event": {
                    "M": {
                    "headers": {
                        "M": {
                        "content-length": {
                            "S": "86"
                        },
                        "referer": {
                            "S": "https://nata.coach/landing/"
                        },
                        "accept-language": {
                            "S": "en-US,en;q=0.8,fr-FR;q=0.5,fr;q=0.3"
                        },
                        "x-forwarded-proto": {
                            "S": "https"
                        },
                        "origin": {
                            "S": "https://nata.coach"
                        },
                        "x-forwarded-port": {
                            "S": "443"
                        },
                        "x-forwarded-for": {
                            "S": "54.239.6.177"
                        },
                        "accept": {
                            "S": "text/html, */*; q=0.01"
                        },
                        "x-amzn-trace-id": {
                            "S": "Root=1-5f96a8ee-6da99b0d095f29287022aa30"
                        },
                        "host": {
                            "S": "vija6eqvi4.execute-api.eu-central-1.amazonaws.com"
                        },
                        "content-type": {
                            "S": "application/x-www-form-urlencoded; charset=UTF-8"
                        },
                        "accept-encoding": {
                            "S": "gzip, deflate, br"
                        },
                        "user-agent": {
                            "S": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:82.0) Gecko/20100101 Firefox/82.0"
                        }
                        }
                    },
                    "isBase64Encoded": {
                        "BOOL": True
                    },
                    "rawPath": {
                        "S": "/prod/form"
                    },
                    "requestContext": {
                        "M": {
                        "accountId": {
                            "S": "401955065246"
                        },
                        "timeEpoch": {
                            "N": "1603709166956"
                        },
                        "routeKey": {
                            "S": "POST /form"
                        },
                        "stage": {
                            "S": "prod"
                        },
                        "domainPrefix": {
                            "S": "vija6eqvi4"
                        },
                        "requestId": {
                            "S": "VA9VWhZHliAEJCA="
                        },
                        "domainName": {
                            "S": "vija6eqvi4.execute-api.eu-central-1.amazonaws.com"
                        },
                        "http": {
                            "M": {
                            "path": {
                                "S": "/prod/form"
                            },
                            "protocol": {
                                "S": "HTTP/1.1"
                            },
                            "method": {
                                "S": "POST"
                            },
                            "sourceIp": {
                                "S": "54.239.6.177"
                            },
                            "userAgent": {
                                "S": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:82.0) Gecko/20100101 Firefox/82.0"
                            }
                            }
                        },
                        "time": {
                            "S": "26/Oct/2020:10:46:06 +0000"
                        },
                        "apiId": {
                            "S": "vija6eqvi4"
                        }
                        }
                    },
                    "routeKey": {
                        "S": "POST /form"
                    },
                    "body": {
                        "S": "cGs9bmF0YS5jb2FjaC5sYW5kaW5nX3BhZ2Umc2s9ZW1haWwmbmFtZT1zdG9ybWFjcSZlbWFpbD1zZWJhc3RpZW4uc3Rvcm1hY3ElNDBnbWFpbC5jb20="
                    },
                    "rawQueryString": {
                        "S": ""
                    },
                    "version": {
                        "S": "2.0"
                    }
                    }
                },
                "email": {
                    "S": "sebastien.stormacq@gmail.com"
                }
                },
                "SequenceNumber": "3133900000000004608185093",
                "SizeBytes": 1323,
                "StreamViewType": "NEW_IMAGE"
            },
            "eventSourceARN": "arn:aws:dynamodb:eu-central-1:401955065246:table/nata-data-collection-form/stream/2020-10-26T12:09:18.744"
            },
            {
            "eventID": "fd797f3039d18236c943d07637301e36",
            "eventName": "REMOVE",
            "eventVersion": "1.1",
            "eventSource": "aws:dynamodb",
            "awsRegion": "eu-central-1",
            "dynamodb": {
                "ApproximateCreationDateTime": 1603714567.0,
                "Keys": {
                "sk": {
                    "S": "sebastien.stormacq@gmail.com"
                },
                "pk": {
                    "S": "nata.coach.landing_page"
                }
                },
                "NewImage": {
                "name": {
                    "S": "stormacq"
                },
                "sk": {
                    "S": "sebastien.stormacq@gmail.com"
                },
                "created_at": {
                    "N": "1603709167"
                },
                "pk": {
                    "S": "nata.coach.landing_page"
                },
                "event": {
                    "M": {
                    "headers": {
                        "M": {
                        "content-length": {
                            "S": "86"
                        },
                        "referer": {
                            "S": "https://nata.coach/landing/"
                        },
                        "accept-language": {
                            "S": "en-US,en;q=0.8,fr-FR;q=0.5,fr;q=0.3"
                        },
                        "x-forwarded-proto": {
                            "S": "https"
                        },
                        "origin": {
                            "S": "https://nata.coach"
                        },
                        "x-forwarded-port": {
                            "S": "443"
                        },
                        "x-forwarded-for": {
                            "S": "54.239.6.177"
                        },
                        "accept": {
                            "S": "text/html, */*; q=0.01"
                        },
                        "x-amzn-trace-id": {
                            "S": "Root=1-5f96a8ee-6da99b0d095f29287022aa30"
                        },
                        "host": {
                            "S": "vija6eqvi4.execute-api.eu-central-1.amazonaws.com"
                        },
                        "content-type": {
                            "S": "application/x-www-form-urlencoded; charset=UTF-8"
                        },
                        "accept-encoding": {
                            "S": "gzip, deflate, br"
                        },
                        "user-agent": {
                            "S": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:82.0) Gecko/20100101 Firefox/82.0"
                        }
                        }
                    },
                    "isBase64Encoded": {
                        "BOOL": True
                    },
                    "rawPath": {
                        "S": "/prod/form"
                    },
                    "requestContext": {
                        "M": {
                        "accountId": {
                            "S": "401955065246"
                        },
                        "timeEpoch": {
                            "N": "1603709166956"
                        },
                        "routeKey": {
                            "S": "POST /form"
                        },
                        "stage": {
                            "S": "prod"
                        },
                        "domainPrefix": {
                            "S": "vija6eqvi4"
                        },
                        "requestId": {
                            "S": "VA9VWhZHliAEJCA="
                        },
                        "domainName": {
                            "S": "vija6eqvi4.execute-api.eu-central-1.amazonaws.com"
                        },
                        "http": {
                            "M": {
                            "path": {
                                "S": "/prod/form"
                            },
                            "protocol": {
                                "S": "HTTP/1.1"
                            },
                            "method": {
                                "S": "POST"
                            },
                            "sourceIp": {
                                "S": "54.239.6.177"
                            },
                            "userAgent": {
                                "S": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:82.0) Gecko/20100101 Firefox/82.0"
                            }
                            }
                        },
                        "time": {
                            "S": "26/Oct/2020:10:46:06 +0000"
                        },
                        "apiId": {
                            "S": "vija6eqvi4"
                        }
                        }
                    },
                    "routeKey": {
                        "S": "POST /form"
                    },
                    "body": {
                        "S": "cGs9bmF0YS5jb2FjaC5sYW5kaW5nX3BhZ2Umc2s9ZW1haWwmbmFtZT1zdG9ybWFjcSZlbWFpbD1zZWJhc3RpZW4uc3Rvcm1hY3ElNDBnbWFpbC5jb20="
                    },
                    "rawQueryString": {
                        "S": ""
                    },
                    "version": {
                        "S": "2.0"
                    }
                    }
                },
                "email": {
                    "S": "sebastien.stormacq@gmail.com"
                }
                },
                "SequenceNumber": "3133900000000004608185093",
                "SizeBytes": 1323,
                "StreamViewType": "NEW_IMAGE"
            },
            "eventSourceARN": "arn:aws:dynamodb:eu-central-1:401955065246:table/nata-data-collection-form/stream/2020-10-26T12:09:18.744"
            },
            {
            "eventID": "fd797f3039d18236c943d07637301e36",
            "eventName": "INSERT",
            "eventVersion": "1.1",
            "eventSource": "aws:dynamodb",
            "awsRegion": "eu-central-1",
            "dynamodb": {
                "ApproximateCreationDateTime": 1603714567.0,
                "Keys": {
                "sk": {
                    "S": "sebastien.stormacq@gmail.com"
                },
                "pk": {
                    "S": "nata.coach.landing_page"
                }
                },
                "NewImage": {
                "name": {
                    "S": "stormacq"
                },
                "sk": {
                    "S": "sebastien.stormacq@gmail.com"
                },
                "created_at": {
                    "N": "1603709167"
                },
                "pk": {
                    "S": "nata.coach.landing_page"
                },
                "event": {
                    "M": {
                    "headers": {
                        "M": {
                        "content-length": {
                            "S": "86"
                        },
                        "referer": {
                            "S": "https://nata.coach/landing/"
                        },
                        "accept-language": {
                            "S": "en-US,en;q=0.8,fr-FR;q=0.5,fr;q=0.3"
                        },
                        "x-forwarded-proto": {
                            "S": "https"
                        },
                        "origin": {
                            "S": "https://nata.coach"
                        },
                        "x-forwarded-port": {
                            "S": "443"
                        },
                        "x-forwarded-for": {
                            "S": "54.239.6.177"
                        },
                        "accept": {
                            "S": "text/html, */*; q=0.01"
                        },
                        "x-amzn-trace-id": {
                            "S": "Root=1-5f96a8ee-6da99b0d095f29287022aa30"
                        },
                        "host": {
                            "S": "vija6eqvi4.execute-api.eu-central-1.amazonaws.com"
                        },
                        "content-type": {
                            "S": "application/x-www-form-urlencoded; charset=UTF-8"
                        },
                        "accept-encoding": {
                            "S": "gzip, deflate, br"
                        },
                        "user-agent": {
                            "S": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:82.0) Gecko/20100101 Firefox/82.0"
                        }
                        }
                    },
                    "isBase64Encoded": {
                        "BOOL": True
                    },
                    "rawPath": {
                        "S": "/prod/form"
                    },
                    "requestContext": {
                        "M": {
                        "accountId": {
                            "S": "401955065246"
                        },
                        "timeEpoch": {
                            "N": "1603709166956"
                        },
                        "routeKey": {
                            "S": "POST /form"
                        },
                        "stage": {
                            "S": "prod"
                        },
                        "domainPrefix": {
                            "S": "vija6eqvi4"
                        },
                        "requestId": {
                            "S": "VA9VWhZHliAEJCA="
                        },
                        "domainName": {
                            "S": "vija6eqvi4.execute-api.eu-central-1.amazonaws.com"
                        },
                        "http": {
                            "M": {
                            "path": {
                                "S": "/prod/form"
                            },
                            "protocol": {
                                "S": "HTTP/1.1"
                            },
                            "method": {
                                "S": "POST"
                            },
                            "sourceIp": {
                                "S": "54.239.6.177"
                            },
                            "userAgent": {
                                "S": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:82.0) Gecko/20100101 Firefox/82.0"
                            }
                            }
                        },
                        "time": {
                            "S": "26/Oct/2020:10:46:06 +0000"
                        },
                        "apiId": {
                            "S": "vija6eqvi4"
                        }
                        }
                    },
                    "routeKey": {
                        "S": "POST /form"
                    },
                    "body": {
                        "S": "cGs9bmF0YS5jb2FjaC5sYW5kaW5nX3BhZ2Umc2s9ZW1haWwmbmFtZT1zdG9ybWFjcSZlbWFpbD1zZWJhc3RpZW4uc3Rvcm1hY3ElNDBnbWFpbC5jb20="
                    },
                    "rawQueryString": {
                        "S": ""
                    },
                    "version": {
                        "S": "2.0"
                    }
                    }
                },
                "email": {
                    "S": "sebastien.stormacq@gmail.com"
                }
                },
                "SequenceNumber": "3133900000000004608185093",
                "SizeBytes": 1323,
                "StreamViewType": "NEW_IMAGE"
            },
            "eventSourceARN": "arn:aws:dynamodb:eu-central-1:401955065246:table/nata-data-collection-form/stream/2020-10-26T12:09:18.744"
            }        
        ]
        }

def test_unauthorized(ddb_event, mocker):
    
    mocker.patch.dict(os.environ, {'SNS_TOPIC_ARN':'arn:aws:sns:eu-central-1:401955065246:DataCollectionTopic'})

    ret = app.lambda_handler(ddb_event, "")

    print(ret)
    assert 'status' in ret
    assert 'ERROR' in ret['status']
    assert 'AuthorizationErrorException' in ret['exception']

def test_happy_path(ddb_event, mocker):
    
    mocker.patch.dict(os.environ, {'SNS_TOPIC_ARN':'arn:aws:sns:eu-central-1:401955065246:DataCollectionTopic'})
    mocker.patch.dict(os.environ, {'UNIT_TEST_PROFILE':'seb'})

    ret = app.lambda_handler(ddb_event, "")

    assert 'status' in ret
    assert ret['status'] == 'OK'
    assert ret['batchSize'] == 1
    assert ret['messages'] == 1

def test_happy_path_multiples(ddb_event_multiple, mocker):
    
    mocker.patch.dict(os.environ, {'SNS_TOPIC_ARN':'arn:aws:sns:eu-central-1:401955065246:DataCollectionTopic'})
    mocker.patch.dict(os.environ, {'UNIT_TEST_PROFILE':'seb'})

    ret = app.lambda_handler(ddb_event_multiple, "")

    assert 'status' in ret
    assert ret['status'] == 'OK'
    assert ret['batchSize'] == 3
    assert ret['messages'] == 2

def test_no_sns_env_var(ddb_event, mocker):
    
    ret = app.lambda_handler(ddb_event, "")

    assert 'status' in ret
    assert 'ERROR' in ret['status']
    assert 'SNS_TOPIC_ARN' in ret['status']
