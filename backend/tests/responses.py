reservation_resp = {
    "viewReservationViewPage": {
        "dates": {"first": "2019-10-25", "second": "2019-10-25"},
        "messages": None,
        "checkInIneligibilityReason": None,
        "greyBoxMessage": None,
        "greyBoxPassengerMessage": None,
        "destinationDescription": "Phoenix",
        "originAirport": {
            "name": "Denver",
            "state": "CO",
            "code": "DEN",
            "country": None,
        },
        "destinationAirport": {
            "name": "Phoenix",
            "state": "AZ",
            "code": "PHX",
            "country": None,
        },
        "companion": None,
        "passengers": [
            {
                "name": "John Doe",
                "accountNumber": "615205662",
                "passengerReference": "2",
                "hasAnyEarlyBird": False,
                "hasCompletePassportInfo": False,
                "checkInIneligibilityReason": None,
                "isCheckedIn": False,
                "isCheckInEligible": False,
                "isUnaccompaniedMinor": False,
            }
        ],
        "confirmationNumber": "MR6D6N",
        "shouldShowAddEarlyBirdButton": False,
        "bounds": [
            {
                "departureStatus": None,
                "departureStatusType": None,
                "arrivalStatus": None,
                "arrivalStatusType": None,
                "flights": [
                    {
                        "number": "3556",
                        "wifiOnBoard": True,
                        "aircraftInfo": {
                            "aircraftType": "Boeing 737-700",
                            "numberOfSeats": 143,
                            "wifiSupported": True,
                        },
                    }
                ],
                "travelTime": "1h 55m",
                "departureDate": "2019-10-25",
                "departureTime": "16:35",
                "departureAirport": {
                    "name": "Denver",
                    "state": "CO",
                    "code": "DEN",
                    "country": None,
                },
                "arrivalTime": "16:35",
                "arrivalAirport": {
                    "name": "Phoenix",
                    "state": "AZ",
                    "code": "PHX",
                    "country": None,
                },
                "passengerTypeCounts": {"adult": 1, "senior": 0},
                "fareType": "Anytime",
                "boundType": "DEPARTING",
                "standbyFlight": None,
                "stops": [],
                "isNextDayArrival": False,
            },
            {
                "departureStatus": None,
                "departureStatusType": None,
                "arrivalStatus": None,
                "arrivalStatusType": None,
                "flights": [
                    {
                        "number": "533",
                        "wifiOnBoard": True,
                        "aircraftInfo": {
                            "aircraftType": "Boeing 737-700",
                            "numberOfSeats": 143,
                            "wifiSupported": True,
                        },
                    }
                ],
                "travelTime": "1h 40m",
                "departureDate": "2019-10-25",
                "departureTime": "15:37",
                "departureAirport": {
                    "name": "Phoenix",
                    "state": "AZ",
                    "code": "PHX",
                    "country": None,
                },
                "arrivalTime": "15:37",
                "arrivalAirport": {
                    "name": "Denver",
                    "state": "CO",
                    "code": "DEN",
                    "country": None,
                },
                "passengerTypeCounts": {"adult": 1, "senior": 0},
                "fareType": "Anytime",
                "boundType": "RETURNING",
                "standbyFlight": None,
                "stops": [],
                "isNextDayArrival": False,
            },
        ],
        "pageHeader": "DEN - PHX",
        "shareDetails": {
            "subject": "Southwest Flight 3556 Denver to Phoenix",
            "confirmationInfo": "Confirmation #: MR6D6N",
            "passengerInfo": "Passenger names: John Doe",
            "flightInfo": [
                {
                    "header": "Departing Flight: Sun, Oct 20, 2019",
                    "title": "Southwest Flight 3556 Denver to Phoenix",
                    "flightInfo": "Flight #: 3556",
                    "departureInfo": "Departs: 16:35 PM DEN",
                    "departureDateTime": "2019-10-25T16:35:00.000-06:00",
                    "stops": None,
                    "arrivalInfo": "Arrives: 01:20 PM PHX",
                    "arrivalDateTime": "2019-10-25T16:35:00.000-07:00",
                    "travelTime": "Travel time: 1hr 55 mins",
                },
                {
                    "header": "Returning Flight: Mon, Oct 21, 2019",
                    "title": "Southwest Flight 533 Phoenix to Denver",
                    "flightInfo": "Flight #: 533",
                    "departureInfo": "Departs: 15:37 AM PHX",
                    "departureDateTime": "2019-10-21T015:37:00.000-07:00",
                    "stops": None,
                    "arrivalInfo": "Arrives: 10:50 AM DEN",
                    "arrivalDateTime": "2019-10-21T15:39:00.000-06:00",
                    "travelTime": "Travel time: 1hr 40 mins",
                },
            ],
        },
        "hasAnyCancelledFlights": False,
        "isCheckInEligible": False,
        "isCheckedIn": False,
        "isInternational": False,
        "isDynamicWaiver": False,
        "isNonRevPnr": False,
        "isSwabiz": False,
        "_links": {
            "checkInSessionToken": None,
            "earlyBird": None,
            "change": None,
            "reaccom": None,
            "cancel": None,
            "viewStandbyList": None,
            "checkIn": None,
            "viewBoardingPassIssuance": None,
            "viewBoardingPositions": None,
            "addCompanion": None,
            "passportEmergencyContacts": None,
            "editPNRPassengers": [
                {
                    "href": "/v1/mobile-air-booking/page/view-reservation/edit-pnr-passenger/MR6D6N",
                    "method": "GET",
                    "query": {
                        "first-name": "John",
                        "last-name": "Doe",
                        "passenger-reference": "2",
                    },
                }
            ],
        },
        "hasUnaccompaniedMinor": False,
    }
}

checkin_get_resp = {
    "checkInSessionToken": "ewogICJwbnIiIDogewogICAgImNvbmZpcm1hdGlvbk51bWJlciIgOiAiTVI2RDZOIiwKICAgICJwYXNzZW5nZXJzIiA6IFsgIk1pY2hhZWwgVGV0bG93IiBdLAogICAgInBhc3NlbmdlcnNOYW1lcyIgOiBbIHsKICAgICAgImZpcnN0TmFtZSIgOiAiTUlDSEFFTCIsCiAgICAgICJsYXN0TmFtZSIgOiAiVEVUTE9XIgogICAgfSBdCiAgfSwKICAiY2FyZHMiIDogWyB7CiAgICAiZGF0ZXMiIDogewogICAgICAiZmlyc3QiIDogIjIwMTktMTAtMjAiCiAgICB9LAogICAgImRlc3RpbmF0aW9uRGVzY3JpcHRpb24iIDogIlBob2VuaXgiLAogICAgImRlcGFydHVyZURhdGUiIDogIjIwMTktMTAtMjAiLAogICAgImRlcGFydHVyZUFpcnBvcnQiIDogIkRFTiIsCiAgICAiZGVwYXJ0dXJlVGltZSIgOiAiMTI6MjUiLAogICAgImFycml2YWxBaXJwb3J0IiA6ICJQSFgiLAogICAgImFycml2YWxUaW1lIiA6ICIxMzoyMCIsCiAgICAiZmxpZ2h0cyIgOiBbIHsKICAgICAgImZsaWdodE51bWJlciIgOiAiMzU1NiIsCiAgICAgICJoYXNXaWZpIiA6IHRydWUsCiAgICAgICJ0cmF2ZWxUaW1lIiA6ICIxaCA1NW0iLAogICAgICAiYXFxU3RhdHVzIiA6ICJUU0FfUFJFX0NIRUNLIiwKICAgICAgIm9yaWdpbkFpcnBvcnRDb2RlIiA6ICJERU4iLAogICAgICAiZGVzdGluYXRpb25BaXJwb3J0Q29kZSIgOiAiUEhYIiwKICAgICAgImRlc3RpbmF0aW9uU3RhdGlvbk5hbWUiIDogIlBob2VuaXgiLAogICAgICAiZGVwYXJ0dXJlRGF0ZSIgOiAiT2N0IDIwIiwKICAgICAgImRlcGFydHVyZUdhdGUiIDogIkM0OSIsCiAgICAgICJkZXBhcnR1cmVUaW1lIiA6ICIxMjoyNSIKICAgIH0gXSwKICAgICJ0cmF2ZWxUaW1lIiA6ICIxaCA1NW0iLAogICAgImludGVybmF0aW9uYWwiIDogZmFsc2UKICB9IF0sCiAgImFpclRyYXZlbFRva2VuIiA6ICJleUpoYkdjaU9pSmthWElpTENKbGJtTWlPaUpCTVRJNFEwSkRMVWhUTWpVMkluMC4uZE45WF9hV3J4R2VYanBKNE5BcDhOZy5EcF9ZRkN4U0xURi13T3VEMTYyXzdySWhOczRWd0IxRFBUWmtBS01Fa3l3anJxeWJSeUh6QnVmMHl4dDU1TklDV1p2Q3J2NG4yV0oxc0I4UUdyRENtMi1idzRyQWRROFUyMF81UVlhd1dfRmI3RWxFbzZLajFwUVJJbzFwLWM1UnQ5T1RTb1ZnSVRWNTliWVl0ZGhNR0xjSTE0dlVfdlJEY0ZrWThtc043OTR3UC1yRE1wZW1yS3BOcFBtN2lQT2gxdG9rZWNKX2NlUVVXR2VKR05MVG41YlJ4WmV3ZTFPaDZROHdsREp6MGc1VFVnaUQzZ25Hdm1Zb3RYRW4wU053WXQ4bWFJNlpuWC1WRGV3a0pMaklmVzc0djgwN2dNelBDLWxvcGZhSVBUeXROWDBfTmd0blpLVFVhQ25SNjVFdk83bFBEcVRqYVFydU5DZFh5VGNCbDgxRmt0YkNDckxqZVhpUjZFNUk5YW9JaDM4akNUN1pBM243QnE4d243VnF6clRfMV9kSnlieG1nSUUtd3N0c0l5M2lLV0VTTV9BWlJ2V0JYNmxGZ1ZKSFZ5UDZELTFOcmJIckRyYkowc0x6WkxpUUJCZDhZdkhqcTVBbGlBYUZnSlZ2bTh5SjE1RkRmQVFPWjV5TXVDUi1GUWV5MzF6Q09zZllHdFpxV2dDb091dk5kVzhNZDVCbTJOa3gtSXZKNjdIcnlXbWl3Z3JlYW1oakM1blpmb2lnQ2dqQlRBY3BZc050Q3VPWWZULWtWQzNpVGlyVk91NWR3OVBMdlhIdnBTcTZtbXotU2p0bnQ1dnliU2J1bUdTZGJFcENYNVpsUTluclhqRXBHeVNDcm80aDNfVWhadHBKVlQycTdfdFBybjkxRWlxakN1Q3p5ZndtQ01VQlpYVGFfWmY1RWZ4SEtLUHdsblltdUd6eWo4Rm9xTXhKUV9WUlplZXd3LWZTakZMdU5EeUxYcmlUb2Qzb29NQXpwZkJ4OUl0VHFVQXdWRTRSVlg2Q2Z5R21IeVlZWjJQa3cxakhzcjE3ejdSNlNtLUM4b1RKMzBuY0x3WnpNd1BOdzdndGJPNWFsUVNHQ2VhMjRCUks5OWVfekYwZER5cHI1RkpKS1hEcVE2REI3MDA3RFNKVEZJM2U2Vl9CZHk0VE5mYmo5SjRGZkhQYkphVjJRMFNrU1lHNWVQMGstYTZBQWFYRE9Gc29vZlRldXhfb09SVVhyRnJLM3lZekd4NFZVT3V3UUZTVEEwdUxwUkhUQ2lGcktwYjdWMFB3V1VUZlY4eUV0NkhBYlZNcWJZaHItUUJIR01JYS0zNDN0a2pwbGtTM0FUUzVCcl9ETUdRZ0RsZl9Rc1BtTzQzUHNHZmxuMGc3S1FsN2hVU011ck9qZDE3VFd0RnBRTE9jQ3dQTkk3MldvTnh3ZmJRVW95ZXl4RV94RVBzTG44MjVBUW95MFlTMWVPSFVwd1JaeVJFUEpVdHRjd1lCYVF4T0gzcnlDRmNzMGNsbUM4amJPTnRmMkhHQzFqN3lyZTYxc2ZkNTFTZ214bjdia1pkN3FrS0VpTjZQajFMYk9IMDVpQnVJb1NrWXNhNTRTV3hiWUdzaVQwTUpUM3pyQm81Q3Z0TXpTVGF1Q1lqRzBpVnFqVVNPQ2ZyYXNld3pMWWNvT1Y2Sllxb3k2dlBHRXZNMUpLdklUY3pmVVZNMUJkbDJNM1ZGN2p3QkVab012WWpwOU4yTWFMQm1DMk5GQlcwaHZ6alhyNDZYMHh4WXMxRE9ycDVXZGFzSUZsdjZkTGg2ZzVEQW9Db0RET3hXZG9MSG45U1NwXzFwZDc0cGdVYmtxTjZEODlMbjhRekJ5QmcxOUlSV2JJQ2VqNjM3LXMzMzF2SW42eko1MXFrWFhBRXloQTBHdUpUTWEwcTFaSkQwMmNLeXhnRFNqNjlmZWQ1VGM1d2gzZzZVWW8zeE9ibElGLUdyM2Q3d1dwS2gtRkdTZTNYZ3RMOVFSSm1MWmJ1TEw1Z0pqOWM4RzBBZ2hud01ZWFJKc2FrV3V1eWszQ21QeWJHdkFnWWNXZllvdlJWbC1FR1lBX0cxNlZJOGZFc0lpR1pIV1drdmc3bUU2OVF2SGFLeEo3c2pLbENwV2dWU0tQTENRS0lvQ08zblBnOXlmakN0d2FMUDRCWV9BUnVIa2g2NXBBeGdWdUV3TVhtQXh6eGdUNFlyNmhlb1pUaVowLXlXQnRjaUxRcHpEWW84Uk5WWEdQekZnVkt1RFg1T3lkcHhmdF9raUhnWDlkaHB1MUtmbmU3cnVGa202ak1WaEJMR2JWajRJRW05TnhEenpKNkRTOW1BRGxXOWRldjBvXy1WZGNkcXB6ejV5bTdteGk2OE03Z3RSYnlZSGh6TFhYVFhMa3M4NDMxdDQ2SGdOSHhVOUxfcWlLRVBmcDVZQXdnLXA4QUN3VENWd0pqUHU5eXlad3ZvR1FrLWxiWF9kYWlUT0dpSkNxQ0x6dFU4M082QXpqNTNhMkVVTV9PNm84RnlvMElrTi1qREMzODBZd3JZeEYyem85U2JPYXNmVlNyUXhoWFhxMzZSb2loekhmWlpkbFpjRm1QQ01kemdLbjBWSEUtdFBxdGd4RnZ6V0V2a3QxdEpETmVOMC1UN01GVHRHZUczM3F0NGlLMFdCQmlkVElKWVFGaVFfMVpDemVfZmIzZWxQdFBoNUxRQk95b3BKbldTTmZSR2ZkdDBHZDh0NXA0QzBWNHEtN3MxMVUxTmRKZjZzZDE1X1A2b2lMbW1rbURFQS1XVnhWSDNzOFE1cHBvSlVFbkhXRDRUck5vcm9jRWZuSFlTVlhxT2I4SGlzMTh2a1oyWUdnZGdBbjBhY3ExUHQ2bzlmamVFUFg5aUl2S25kZmg0dUZseTA1ZGVQcnlKRUJoS2E5VFdNdGNuRnhRYTZnZTgtTjV1WmFJNU5kUzRvRlFpV3BmVjBKVmZUemdjaUVrTnNzbjFHWjYwR2FaRlJ2enMzMjJFLWYwblQtUlJDREdYNGc5SmhzdkJGNnhSbHNNeS1Ga0dyYVVZZ0c0SUdCRjNGQ0JuS2IwSkdST3hyaEh2TElaczE4NC1SSFA0bUlyMDlaRy1DeEV6U2FFR1h2S3BLdVFqSTZXZXdjdHltSl8zcm9sTDhoY0FHN3ctcnFQVHd6TEJvV19iN1hzamY3UFVaYjJPZVRCOEZIckdVNGtKdUNNSkpXVW5lejB6MHhGR2ZTOHpNS1VRb1dyZHJGU3FybHBQRzd1ajB0TEVwa01tU1JVOWFYRFFLMlprcHNfQmxiWlJGdFd2bjAzeWxmOGVUcGJ2SXRZZkttZEc2RXYtUFZUcVh1NVJ0Zm1xN2x2alZrMGg4eXdrbDVMenJRR2lBaWV6VkVzN01xTzRkQTRZZWpwb05qS1dKal9ESjdZYWlpdTVWekV4cEtmUC1qWDNET2E2TVhCakRvRjhLeXR3NEYwZXozQ3I3QmxEZHhON0oyNEVmSEVIRFVGUTA1NzVZRnRzWVdTeXRaM284X2h0bW94dzlkQnhVZlotajY3TmdTNjFwTjJ5bzNMY3F1MXZkVzBvSFhPUXdHVXM2MEdNV0pHVWRpMjkwS1JJWEJ6bFRBTElQb1ZPaHJ5V2hrUWdCWFJ4Z0RTcWp5WFc5TjVnbUdsN2c1ajRRcE9kWEd5LTRTcENFV3dwdm9rR3pTMVR1akRsMGM1aU4waWF5SGJWazV6SkJFbTVmeGNMT0Q4azJtZmxkc0ZKQ1VFdlhycTdnbzREZ2FEUEc2TE1SdlZDTks4S2x5cUVrdkt3QnU0a2pkNmNXbmRyeHJoMUJET1lrTjZfcE1jSnhQUWp0T09HMFBsWFBmRmlsMDFpbkozNklYOTlvd1M3ZDhrVGxmdS15WXBmMXVzR1hMVGRYSWNYeE1NaW9TZUlfeExmRmxZM1B2cXdZNUI3cU9uNTZIbzN6TS1JVW5XV3BpYnNCUzc2N2ZaN0JiT1M3aDVaalJkam4wRVRrWnluNVE5MENXTGZxd2lzOHFkdFVQZGNoaDhOQnEzeC1LMUg5b2VqTkVLdWhTQ2FYTGwySmZOdVk4TjFScXVKSTVFQlRxb3Vjd0h5UUh6SjRFcW1vODlzd2x2cTZQcFZpMk45WWdpaUY4bWpicUJGNjJaSjN1SngyamFBNWtIUXAwekV6clVBOWwzck9XdVRxa2YySm05UHIwMDQ2bzZsMDdrNGlaRHJsTF94M1NkdU4zVVh0b2pNUDRQVDJKZ19aQ0xuXzRQNGlYWThFaXNmUjFzUk9YYTJjZ21tLWtqRGlOZmprQVFTc2R2TVNIS2xScVlaTExKSUpQbjl4ZmEyYkV5RGJVOWdNNDJMejFMRENZVkpRY2E0YWgtNFJCSWdoMWhCWnVJSU5MZzhpVGlFOFhCLWtWWFUzUDZQeGFMeG5EY1hDcnhmYTFLLVB0Y1VzXzE3WVI2bERQWjlGOEdWOFJPSXI3NDhmbTd1MW5zSDNPOGxOYklGTGotRkp3eDZFdDRjSDhyWkg2cWJQNjEwd0pRcWdMRW9rNkJybnRkSTZDN2syS1FLaXFoY2Y5eTVMMG5wbE5FM3BoMTRmdXV2cVlVLVBadXoxdDFFLXVlWU9rTXBUNXdNeHR3LWZhWUd5ME1Uc29LcVBIRnl4MkhNaHMxMUxuWk5VYjRWUGtnSDA0UUh5bTd0VWV2NWVBcnE5OXA0T1NvQk5qNTJjbi0yWmxuSEhOMU1ZamhFWjRvbHQ4dFlsbkxFWmNqVGRETlpfOVpRVXl4VGY4ZmdRUVlSVGJCME9TRzJoa25SSjZpN1BTSnZibFhTMVR5TFFMT2E1dGJ2NFgyempfckdGTUdtQS1obklzMzFpNmRUc1hVUkhSQ216YzJnakx5ZENsTHJPa3drOVM4azd1OG5FaU5UaUY3X2NZRG9tNjZpNlBVOFlWUnBEbzhDay05dENWQjBaMGgtVm5KTHctQjVFX2sySkVocjkwWkNYZUlBMWotNG9uRDdFWXdXeHE0b1FRMzJYa1k0bW9ZUV9JVVRuUnd0aFBhVnBfa1doNFNmNGpNWnpnNjhOUzdUVmxOUVJsYVdMVTFiUXpUNTNrSHMwTjVrS3ZnNFR5RldpX1RWMk1QcVRPT1lvQ0NncjZhNmFYSlU4Vk82amdzUFVTNWFsbFVjN2l1LW45NnJrb1VfaEgzWjZzd2FoMG1UR1RKTFlDS1loT09aUjRsZXZYZ3haRVd6UlRQQ2RETjVkWHJHeXh0QXJQcEVmOWJaV2RBUC1YRzBRWTZJbWZpa2ZuTHhNV0lza2thRTVLMHRnV2lYbG1ia05TVjZQMzk0Z3MtVERIS0hEazRxT1BwenI5b3hFZ2MtU0Z6WnltblMweFd2cWUwRmZLU3BQdFBBTjBHcExfMUQzVVRwTHdYVno5WFBqYUNkbnBIOGR1VkYzQ3NGZU50a0ZSMEFjTUgweVZHbmN4T0Z4UjNMd3FJZmZOQUlOTXhDTC1uUXpORjFCOWZ2ZE16WnR2RVpqZnBoVXNkcVdUUnhlaEJKRC15RzZDR2hRWkhMblhMc0ItdHhKQURadTZxS2xPUGVLak4xdFBQT09RdkxrNUpRRnNid0ZvUV9HUks3MGI5UmhoMzFrdVNXRUs1V19OUjhqOFc5UnFyX1JJcmE3Slk5eFQta2d4STYzRTRHd1Y4WWxiMFZPNm5HcUl6N1BiSkRkbEQ4dUJfNHlFbW9aWlcyZzdLN2VJRGhRQ2VxSjJUWmh4Y2ZESU5UN0lvYzFXeEtiRFowMHVsWXJmbjFCUDVJMlEwMWdMdzdDQU94Zm1OZHVjdWZNdnNXOEhUV09CV1BJWm5qbVpnYWlCblhucUwtbC16cHUzRHF5WEFRN3hLRjJCQUJjVXBiUmVHdmZVVURnYnQzUXBZRkpUUEFxZXA4QzF4UUowVkYzOGhnRjA5eVJnal8xVGFvS3lXbnZXRWJqTjFjVUgwT195cElyYlRxRlJIQVNOdzk4amxxOWZfdkZnaXJNR1pvRm9jTGFtQWhQUXV1V0Y4Y0txZTN0TW1OWkdUMVBzQWtSTnI5QTVBTHFCOTU2VlNTNjNycnB4Zjg3dWV4MVNGeDBhOGpaWTR3dEQ0cVg2c3FFcWF2emk0cUxNWDF2RUtlckZuNHJsMG9MRExCMEI5QUkzUzZnOTd5eUVMVF9wWU0xVjhhYUlNTnhJMU53XzJIMEhyYzN1ZVJlTktkR1VTTW50Sl91d0JCdWpXWk9hQmFyQlctVDRFMDRHNnQ4MFREMmVoRU5oRDl1RU5COWxxRTJ0YkJqalNBSldHMGNQV0R3RzBiR3VSUUFGOHRidTRYQ2x1M3J3d0t2THFENy02dDBSbzlqX3MzdExiNGREb2VUdzhReEpDRlVkNlcxajVYemFUWDVidjIxb2pqdUZyLWtfNTNoeDZ0cFFIYXduN2o1eENOcHRVRVZGNTRvZTJWU21CVjhOZUZNNHE1SEw3NS1Kam0ydy5rMHktRXZOd21ZMG5Icjh1TExmbXF3IiwKICAiX2xpbmtzIiA6IHsKICAgICJ0cmF2ZWxEb2N1bWVudHMiIDogWyB7CiAgICAgICJib2R5IiA6IHsKICAgICAgICAicmVjb3JkTG9jYXRvciIgOiAiTVI2RDZOIiwKICAgICAgICAidHJhdmVsZXJJZGVudGlmaWVyIiA6ICIyMDA1Q0NFMDAwMDM1OUNBIiwKICAgICAgICAiZmlyc3ROYW1lIiA6ICJNSUNIQUVMIiwKICAgICAgICAibGFzdE5hbWUiIDogIlRFVExPVyIsCiAgICAgICAgImZ1bGxOYW1lIiA6ICJNaWNoYWVsIFRldGxvdyIsCiAgICAgICAgImFjY291bnROdW1iZXIiIDogIjYxNTIwNTY2MiIsCiAgICAgICAgImVsaWdpYmxlRm9yRHJpbmtDb3Vwb24iIDogZmFsc2UsCiAgICAgICAgInBhc3NlbmdlclR5cGUiIDogIkEiCiAgICAgIH0sCiAgICAgICJib2FyZGluZ0JvdW5kcyIgOiBbIHsKICAgICAgICAiaW5kZXgiIDogMSwKICAgICAgICAiYm9hcmRpbmdTZWdtZW50cyIgOiBbIHsKICAgICAgICAgICJ0cmF2ZWxlclNlZ21lbnRJZGVudGlmaWVyIiA6ICIyMDAwMUNFMDAwMTRCMTE3IiwKICAgICAgICAgICJlbGVnaWJsZUZvckRyaW5rQ291cG9uIiA6IGZhbHNlLAogICAgICAgICAgImJvYXJkaW5nRGV0YWlscyIgOiB7CiAgICAgICAgICAgICJjdXN0b21lckFjY2VwdGFuY2VTdGF0dXMiIDogIk5PVF9BQ0NFUFRFRCIsCiAgICAgICAgICAgICJzZWdtZW50U3RhdHVzIiA6IHsKICAgICAgICAgICAgICAiZ2VuZXJhbFN0YXR1cyIgOiAiT1BFTiIKICAgICAgICAgICAgfQogICAgICAgICAgfSwKICAgICAgICAgICJoYXNUc2FQcmVjaGVjayIgOiB0cnVlLAogICAgICAgICAgInZhbGlkQXFxU3RhdHVzIiA6IHRydWUsCiAgICAgICAgICAic2VnbWVudEJvb2tpbmdTdGF0dXMiIDogIkNPTkZJUk1FRCIKICAgICAgICB9IF0KICAgICAgfSBdCiAgICB9IF0KICB9Cn0=",
    "checkInViewReservationPage": {
        "pnr": {"confirmationNumber": "MR6D6N", "passengers": ["John Doe"]},
        "cards": [
            {
                "dates": {"first": "2019-10-25", "second": None},
                "destinationDescription": "Phoenix",
                "departureDate": "2019-10-25",
                "departureAirport": "DEN",
                "departureTime": "16:35",
                "arrivalAirport": "PHX",
                "arrivalTime": "16:55",
                "hazmatCheckInDisclaimer": "By tapping 'Check in' you acknowledge that you understand the hazardous materials restrictions and penalties.",
                "flights": [
                    {
                        "flightNumber": "3556",
                        "hasWifi": True,
                        "originAirportCode": "DEN",
                        "destinationAirportCode": "PHX",
                        "destinationStationName": "Phoenix",
                        "departureDate": "Oct 20",
                        "departureGate": "C49",
                        "departureTime": "16:35",
                    }
                ],
                "travelTime": "1h 55m",
            }
        ],
        "hazmatText": "Federal law forbids the carriage of hazardous materials such as aerosols, fireworks, lithium batteries and flammable liquids aboard the aircraft in your checked or carryon baggage. E-cigarettes are not permitted in checked baggage and must be transported in carryon baggage only.",
        "_links": {
            "checkIn": {
                "href": "/v1/mobile-air-operations/page/check-in",
                "method": "POST",
                "body": {
                    "recordLocator": "MR6D6N",
                    "checkInSessionToken": "ewogICJwbnIiIDogewogICAgImNvbmZpcm1hdGlvbk51bWJlciIgOiAiTVI2RDZOIiwKICAgICJwYXNzZW5nZXJzIiA6IFsgIk1pY2hhZWwgVGV0bG93IiBdLAogICAgInBhc3NlbmdlcnNOYW1lcyIgOiBbIHsKICAgICAgImZpcnN0TmFtZSIgOiAiTUlDSEFFTCIsCiAgICAgICJsYXN0TmFtZSIgOiAiVEVUTE9XIgogICAgfSBdCiAgfSwKICAiY2FyZHMiIDogWyB7CiAgICAiZGF0ZXMiIDogewogICAgICAiZmlyc3QiIDogIjIwMTktMTAtMjAiCiAgICB9LAogICAgImRlc3RpbmF0aW9uRGVzY3JpcHRpb24iIDogIlBob2VuaXgiLAogICAgImRlcGFydHVyZURhdGUiIDogIjIwMTktMTAtMjAiLAogICAgImRlcGFydHVyZUFpcnBvcnQiIDogIkRFTiIsCiAgICAiZGVwYXJ0dXJlVGltZSIgOiAiMTI6MjUiLAogICAgImFycml2YWxBaXJwb3J0IiA6ICJQSFgiLAogICAgImFycml2YWxUaW1lIiA6ICIxMzoyMCIsCiAgICAiZmxpZ2h0cyIgOiBbIHsKICAgICAgImZsaWdodE51bWJlciIgOiAiMzU1NiIsCiAgICAgICJoYXNXaWZpIiA6IHRydWUsCiAgICAgICJ0cmF2ZWxUaW1lIiA6ICIxaCA1NW0iLAogICAgICAiYXFxU3RhdHVzIiA6ICJUU0FfUFJFX0NIRUNLIiwKICAgICAgIm9yaWdpbkFpcnBvcnRDb2RlIiA6ICJERU4iLAogICAgICAiZGVzdGluYXRpb25BaXJwb3J0Q29kZSIgOiAiUEhYIiwKICAgICAgImRlc3RpbmF0aW9uU3RhdGlvbk5hbWUiIDogIlBob2VuaXgiLAogICAgICAiZGVwYXJ0dXJlRGF0ZSIgOiAiT2N0IDIwIiwKICAgICAgImRlcGFydHVyZUdhdGUiIDogIkM0OSIsCiAgICAgICJkZXBhcnR1cmVUaW1lIiA6ICIxMjoyNSIKICAgIH0gXSwKICAgICJ0cmF2ZWxUaW1lIiA6ICIxaCA1NW0iLAogICAgImludGVybmF0aW9uYWwiIDogZmFsc2UKICB9IF0sCiAgImFpclRyYXZlbFRva2VuIiA6ICJleUpoYkdjaU9pSmthWElpTENKbGJtTWlPaUpCTVRJNFEwSkRMVWhUTWpVMkluMC4uZE45WF9hV3J4R2VYanBKNE5BcDhOZy5EcF9ZRkN4U0xURi13T3VEMTYyXzdySWhOczRWd0IxRFBUWmtBS01Fa3l3anJxeWJSeUh6QnVmMHl4dDU1TklDV1p2Q3J2NG4yV0oxc0I4UUdyRENtMi1idzRyQWRROFUyMF81UVlhd1dfRmI3RWxFbzZLajFwUVJJbzFwLWM1UnQ5T1RTb1ZnSVRWNTliWVl0ZGhNR0xjSTE0dlVfdlJEY0ZrWThtc043OTR3UC1yRE1wZW1yS3BOcFBtN2lQT2gxdG9rZWNKX2NlUVVXR2VKR05MVG41YlJ4WmV3ZTFPaDZROHdsREp6MGc1VFVnaUQzZ25Hdm1Zb3RYRW4wU053WXQ4bWFJNlpuWC1WRGV3a0pMaklmVzc0djgwN2dNelBDLWxvcGZhSVBUeXROWDBfTmd0blpLVFVhQ25SNjVFdk83bFBEcVRqYVFydU5DZFh5VGNCbDgxRmt0YkNDckxqZVhpUjZFNUk5YW9JaDM4akNUN1pBM243QnE4d243VnF6clRfMV9kSnlieG1nSUUtd3N0c0l5M2lLV0VTTV9BWlJ2V0JYNmxGZ1ZKSFZ5UDZELTFOcmJIckRyYkowc0x6WkxpUUJCZDhZdkhqcTVBbGlBYUZnSlZ2bTh5SjE1RkRmQVFPWjV5TXVDUi1GUWV5MzF6Q09zZllHdFpxV2dDb091dk5kVzhNZDVCbTJOa3gtSXZKNjdIcnlXbWl3Z3JlYW1oakM1blpmb2lnQ2dqQlRBY3BZc050Q3VPWWZULWtWQzNpVGlyVk91NWR3OVBMdlhIdnBTcTZtbXotU2p0bnQ1dnliU2J1bUdTZGJFcENYNVpsUTluclhqRXBHeVNDcm80aDNfVWhadHBKVlQycTdfdFBybjkxRWlxakN1Q3p5ZndtQ01VQlpYVGFfWmY1RWZ4SEtLUHdsblltdUd6eWo4Rm9xTXhKUV9WUlplZXd3LWZTakZMdU5EeUxYcmlUb2Qzb29NQXpwZkJ4OUl0VHFVQXdWRTRSVlg2Q2Z5R21IeVlZWjJQa3cxakhzcjE3ejdSNlNtLUM4b1RKMzBuY0x3WnpNd1BOdzdndGJPNWFsUVNHQ2VhMjRCUks5OWVfekYwZER5cHI1RkpKS1hEcVE2REI3MDA3RFNKVEZJM2U2Vl9CZHk0VE5mYmo5SjRGZkhQYkphVjJRMFNrU1lHNWVQMGstYTZBQWFYRE9Gc29vZlRldXhfb09SVVhyRnJLM3lZekd4NFZVT3V3UUZTVEEwdUxwUkhUQ2lGcktwYjdWMFB3V1VUZlY4eUV0NkhBYlZNcWJZaHItUUJIR01JYS0zNDN0a2pwbGtTM0FUUzVCcl9ETUdRZ0RsZl9Rc1BtTzQzUHNHZmxuMGc3S1FsN2hVU011ck9qZDE3VFd0RnBRTE9jQ3dQTkk3MldvTnh3ZmJRVW95ZXl4RV94RVBzTG44MjVBUW95MFlTMWVPSFVwd1JaeVJFUEpVdHRjd1lCYVF4T0gzcnlDRmNzMGNsbUM4amJPTnRmMkhHQzFqN3lyZTYxc2ZkNTFTZ214bjdia1pkN3FrS0VpTjZQajFMYk9IMDVpQnVJb1NrWXNhNTRTV3hiWUdzaVQwTUpUM3pyQm81Q3Z0TXpTVGF1Q1lqRzBpVnFqVVNPQ2ZyYXNld3pMWWNvT1Y2Sllxb3k2dlBHRXZNMUpLdklUY3pmVVZNMUJkbDJNM1ZGN2p3QkVab012WWpwOU4yTWFMQm1DMk5GQlcwaHZ6alhyNDZYMHh4WXMxRE9ycDVXZGFzSUZsdjZkTGg2ZzVEQW9Db0RET3hXZG9MSG45U1NwXzFwZDc0cGdVYmtxTjZEODlMbjhRekJ5QmcxOUlSV2JJQ2VqNjM3LXMzMzF2SW42eko1MXFrWFhBRXloQTBHdUpUTWEwcTFaSkQwMmNLeXhnRFNqNjlmZWQ1VGM1d2gzZzZVWW8zeE9ibElGLUdyM2Q3d1dwS2gtRkdTZTNYZ3RMOVFSSm1MWmJ1TEw1Z0pqOWM4RzBBZ2hud01ZWFJKc2FrV3V1eWszQ21QeWJHdkFnWWNXZllvdlJWbC1FR1lBX0cxNlZJOGZFc0lpR1pIV1drdmc3bUU2OVF2SGFLeEo3c2pLbENwV2dWU0tQTENRS0lvQ08zblBnOXlmakN0d2FMUDRCWV9BUnVIa2g2NXBBeGdWdUV3TVhtQXh6eGdUNFlyNmhlb1pUaVowLXlXQnRjaUxRcHpEWW84Uk5WWEdQekZnVkt1RFg1T3lkcHhmdF9raUhnWDlkaHB1MUtmbmU3cnVGa202ak1WaEJMR2JWajRJRW05TnhEenpKNkRTOW1BRGxXOWRldjBvXy1WZGNkcXB6ejV5bTdteGk2OE03Z3RSYnlZSGh6TFhYVFhMa3M4NDMxdDQ2SGdOSHhVOUxfcWlLRVBmcDVZQXdnLXA4QUN3VENWd0pqUHU5eXlad3ZvR1FrLWxiWF9kYWlUT0dpSkNxQ0x6dFU4M082QXpqNTNhMkVVTV9PNm84RnlvMElrTi1qREMzODBZd3JZeEYyem85U2JPYXNmVlNyUXhoWFhxMzZSb2loekhmWlpkbFpjRm1QQ01kemdLbjBWSEUtdFBxdGd4RnZ6V0V2a3QxdEpETmVOMC1UN01GVHRHZUczM3F0NGlLMFdCQmlkVElKWVFGaVFfMVpDemVfZmIzZWxQdFBoNUxRQk95b3BKbldTTmZSR2ZkdDBHZDh0NXA0QzBWNHEtN3MxMVUxTmRKZjZzZDE1X1A2b2lMbW1rbURFQS1XVnhWSDNzOFE1cHBvSlVFbkhXRDRUck5vcm9jRWZuSFlTVlhxT2I4SGlzMTh2a1oyWUdnZGdBbjBhY3ExUHQ2bzlmamVFUFg5aUl2S25kZmg0dUZseTA1ZGVQcnlKRUJoS2E5VFdNdGNuRnhRYTZnZTgtTjV1WmFJNU5kUzRvRlFpV3BmVjBKVmZUemdjaUVrTnNzbjFHWjYwR2FaRlJ2enMzMjJFLWYwblQtUlJDREdYNGc5SmhzdkJGNnhSbHNNeS1Ga0dyYVVZZ0c0SUdCRjNGQ0JuS2IwSkdST3hyaEh2TElaczE4NC1SSFA0bUlyMDlaRy1DeEV6U2FFR1h2S3BLdVFqSTZXZXdjdHltSl8zcm9sTDhoY0FHN3ctcnFQVHd6TEJvV19iN1hzamY3UFVaYjJPZVRCOEZIckdVNGtKdUNNSkpXVW5lejB6MHhGR2ZTOHpNS1VRb1dyZHJGU3FybHBQRzd1ajB0TEVwa01tU1JVOWFYRFFLMlprcHNfQmxiWlJGdFd2bjAzeWxmOGVUcGJ2SXRZZkttZEc2RXYtUFZUcVh1NVJ0Zm1xN2x2alZrMGg4eXdrbDVMenJRR2lBaWV6VkVzN01xTzRkQTRZZWpwb05qS1dKal9ESjdZYWlpdTVWekV4cEtmUC1qWDNET2E2TVhCakRvRjhLeXR3NEYwZXozQ3I3QmxEZHhON0oyNEVmSEVIRFVGUTA1NzVZRnRzWVdTeXRaM284X2h0bW94dzlkQnhVZlotajY3TmdTNjFwTjJ5bzNMY3F1MXZkVzBvSFhPUXdHVXM2MEdNV0pHVWRpMjkwS1JJWEJ6bFRBTElQb1ZPaHJ5V2hrUWdCWFJ4Z0RTcWp5WFc5TjVnbUdsN2c1ajRRcE9kWEd5LTRTcENFV3dwdm9rR3pTMVR1akRsMGM1aU4waWF5SGJWazV6SkJFbTVmeGNMT0Q4azJtZmxkc0ZKQ1VFdlhycTdnbzREZ2FEUEc2TE1SdlZDTks4S2x5cUVrdkt3QnU0a2pkNmNXbmRyeHJoMUJET1lrTjZfcE1jSnhQUWp0T09HMFBsWFBmRmlsMDFpbkozNklYOTlvd1M3ZDhrVGxmdS15WXBmMXVzR1hMVGRYSWNYeE1NaW9TZUlfeExmRmxZM1B2cXdZNUI3cU9uNTZIbzN6TS1JVW5XV3BpYnNCUzc2N2ZaN0JiT1M3aDVaalJkam4wRVRrWnluNVE5MENXTGZxd2lzOHFkdFVQZGNoaDhOQnEzeC1LMUg5b2VqTkVLdWhTQ2FYTGwySmZOdVk4TjFScXVKSTVFQlRxb3Vjd0h5UUh6SjRFcW1vODlzd2x2cTZQcFZpMk45WWdpaUY4bWpicUJGNjJaSjN1SngyamFBNWtIUXAwekV6clVBOWwzck9XdVRxa2YySm05UHIwMDQ2bzZsMDdrNGlaRHJsTF94M1NkdU4zVVh0b2pNUDRQVDJKZ19aQ0xuXzRQNGlYWThFaXNmUjFzUk9YYTJjZ21tLWtqRGlOZmprQVFTc2R2TVNIS2xScVlaTExKSUpQbjl4ZmEyYkV5RGJVOWdNNDJMejFMRENZVkpRY2E0YWgtNFJCSWdoMWhCWnVJSU5MZzhpVGlFOFhCLWtWWFUzUDZQeGFMeG5EY1hDcnhmYTFLLVB0Y1VzXzE3WVI2bERQWjlGOEdWOFJPSXI3NDhmbTd1MW5zSDNPOGxOYklGTGotRkp3eDZFdDRjSDhyWkg2cWJQNjEwd0pRcWdMRW9rNkJybnRkSTZDN2syS1FLaXFoY2Y5eTVMMG5wbE5FM3BoMTRmdXV2cVlVLVBadXoxdDFFLXVlWU9rTXBUNXdNeHR3LWZhWUd5ME1Uc29LcVBIRnl4MkhNaHMxMUxuWk5VYjRWUGtnSDA0UUh5bTd0VWV2NWVBcnE5OXA0T1NvQk5qNTJjbi0yWmxuSEhOMU1ZamhFWjRvbHQ4dFlsbkxFWmNqVGRETlpfOVpRVXl4VGY4ZmdRUVlSVGJCME9TRzJoa25SSjZpN1BTSnZibFhTMVR5TFFMT2E1dGJ2NFgyempfckdGTUdtQS1obklzMzFpNmRUc1hVUkhSQ216YzJnakx5ZENsTHJPa3drOVM4azd1OG5FaU5UaUY3X2NZRG9tNjZpNlBVOFlWUnBEbzhDay05dENWQjBaMGgtVm5KTHctQjVFX2sySkVocjkwWkNYZUlBMWotNG9uRDdFWXdXeHE0b1FRMzJYa1k0bW9ZUV9JVVRuUnd0aFBhVnBfa1doNFNmNGpNWnpnNjhOUzdUVmxOUVJsYVdMVTFiUXpUNTNrSHMwTjVrS3ZnNFR5RldpX1RWMk1QcVRPT1lvQ0NncjZhNmFYSlU4Vk82amdzUFVTNWFsbFVjN2l1LW45NnJrb1VfaEgzWjZzd2FoMG1UR1RKTFlDS1loT09aUjRsZXZYZ3haRVd6UlRQQ2RETjVkWHJHeXh0QXJQcEVmOWJaV2RBUC1YRzBRWTZJbWZpa2ZuTHhNV0lza2thRTVLMHRnV2lYbG1ia05TVjZQMzk0Z3MtVERIS0hEazRxT1BwenI5b3hFZ2MtU0Z6WnltblMweFd2cWUwRmZLU3BQdFBBTjBHcExfMUQzVVRwTHdYVno5WFBqYUNkbnBIOGR1VkYzQ3NGZU50a0ZSMEFjTUgweVZHbmN4T0Z4UjNMd3FJZmZOQUlOTXhDTC1uUXpORjFCOWZ2ZE16WnR2RVpqZnBoVXNkcVdUUnhlaEJKRC15RzZDR2hRWkhMblhMc0ItdHhKQURadTZxS2xPUGVLak4xdFBQT09RdkxrNUpRRnNid0ZvUV9HUks3MGI5UmhoMzFrdVNXRUs1V19OUjhqOFc5UnFyX1JJcmE3Slk5eFQta2d4STYzRTRHd1Y4WWxiMFZPNm5HcUl6N1BiSkRkbEQ4dUJfNHlFbW9aWlcyZzdLN2VJRGhRQ2VxSjJUWmh4Y2ZESU5UN0lvYzFXeEtiRFowMHVsWXJmbjFCUDVJMlEwMWdMdzdDQU94Zm1OZHVjdWZNdnNXOEhUV09CV1BJWm5qbVpnYWlCblhucUwtbC16cHUzRHF5WEFRN3hLRjJCQUJjVXBiUmVHdmZVVURnYnQzUXBZRkpUUEFxZXA4QzF4UUowVkYzOGhnRjA5eVJnal8xVGFvS3lXbnZXRWJqTjFjVUgwT195cElyYlRxRlJIQVNOdzk4amxxOWZfdkZnaXJNR1pvRm9jTGFtQWhQUXV1V0Y4Y0txZTN0TW1OWkdUMVBzQWtSTnI5QTVBTHFCOTU2VlNTNjNycnB4Zjg3dWV4MVNGeDBhOGpaWTR3dEQ0cVg2c3FFcWF2emk0cUxNWDF2RUtlckZuNHJsMG9MRExCMEI5QUkzUzZnOTd5eUVMVF9wWU0xVjhhYUlNTnhJMU53XzJIMEhyYzN1ZVJlTktkR1VTTW50Sl91d0JCdWpXWk9hQmFyQlctVDRFMDRHNnQ4MFREMmVoRU5oRDl1RU5COWxxRTJ0YkJqalNBSldHMGNQV0R3RzBiR3VSUUFGOHRidTRYQ2x1M3J3d0t2THFENy02dDBSbzlqX3MzdExiNGREb2VUdzhReEpDRlVkNlcxajVYemFUWDVidjIxb2pqdUZyLWtfNTNoeDZ0cFFIYXduN2o1eENOcHRVRVZGNTRvZTJWU21CVjhOZUZNNHE1SEw3NS1Kam0ydy5rMHktRXZOd21ZMG5Icjh1TExmbXF3IiwKICAiX2xpbmtzIiA6IHsKICAgICJ0cmF2ZWxEb2N1bWVudHMiIDogWyB7CiAgICAgICJib2R5IiA6IHsKICAgICAgICAicmVjb3JkTG9jYXRvciIgOiAiTVI2RDZOIiwKICAgICAgICAidHJhdmVsZXJJZGVudGlmaWVyIiA6ICIyMDA1Q0NFMDAwMDM1OUNBIiwKICAgICAgICAiZmlyc3ROYW1lIiA6ICJNSUNIQUVMIiwKICAgICAgICAibGFzdE5hbWUiIDogIlRFVExPVyIsCiAgICAgICAgImZ1bGxOYW1lIiA6ICJNaWNoYWVsIFRldGxvdyIsCiAgICAgICAgImFjY291bnROdW1iZXIiIDogIjYxNTIwNTY2MiIsCiAgICAgICAgImVsaWdpYmxlRm9yRHJpbmtDb3Vwb24iIDogZmFsc2UsCiAgICAgICAgInBhc3NlbmdlclR5cGUiIDogIkEiCiAgICAgIH0sCiAgICAgICJib2FyZGluZ0JvdW5kcyIgOiBbIHsKICAgICAgICAiaW5kZXgiIDogMSwKICAgICAgICAiYm9hcmRpbmdTZWdtZW50cyIgOiBbIHsKICAgICAgICAgICJ0cmF2ZWxlclNlZ21lbnRJZGVudGlmaWVyIiA6ICIyMDAwMUNFMDAwMTRCMTE3IiwKICAgICAgICAgICJlbGVnaWJsZUZvckRyaW5rQ291cG9uIiA6IGZhbHNlLAogICAgICAgICAgImJvYXJkaW5nRGV0YWlscyIgOiB7CiAgICAgICAgICAgICJjdXN0b21lckFjY2VwdGFuY2VTdGF0dXMiIDogIk5PVF9BQ0NFUFRFRCIsCiAgICAgICAgICAgICJzZWdtZW50U3RhdHVzIiA6IHsKICAgICAgICAgICAgICAiZ2VuZXJhbFN0YXR1cyIgOiAiT1BFTiIKICAgICAgICAgICAgfQogICAgICAgICAgfSwKICAgICAgICAgICJoYXNUc2FQcmVjaGVjayIgOiB0cnVlLAogICAgICAgICAgInZhbGlkQXFxU3RhdHVzIiA6IHRydWUsCiAgICAgICAgICAic2VnbWVudEJvb2tpbmdTdGF0dXMiIDogIkNPTkZJUk1FRCIKICAgICAgICB9IF0KICAgICAgfSBdCiAgICB9IF0KICB9Cn0=",
                    "firstName": "John",
                    "lastName": "Doe",
                },
            },
            "travelDocuments": None,
        },
    },
    "prefillPassengerAPISDocuments": None,
}

checkin_post_resp = {
    "checkInConfirmationPage": {
        "messages": None,
        "title": {
            "key": "CHECKIN__YOURE_CHECKEDIN",
            "body": "You're checked in!",
            "icon": "SUCCESS",
            "textColor": "NORMAL",
        },
        "flights": [
            {
                "boundIndex": 0,
                "segmentType": "DEPARTING",
                "departureTime": "16:35",
                "gate": "C49",
                "passengers": [
                    {
                        "name": "John Doe",
                        "hasPrecheck": True,
                        "boardingGroup": "B",
                        "boardingPosition": "55",
                        "mobileBoardingPassEligible": True,
                        "mobileBoardingPassIneligibilityErrorCode": "",
                        "greyBoxMessage": None,
                        "specialAssistanceMessage": None,
                        "travelerSegmentIdentifier": "20001CE00014B117",
                        "travelerID": "2005CCE0000359CA",
                        "checkedIn": True,
                        "confirmationNumber": "MR6D6N",
                        "_links": {
                            "viewPassengerBoardingPass": {
                                "href": "/v1/mobile-air-operations/page/check-in/retrieve-boarding-pass/MR6D6N",
                                "method": "POST",
                                "body": {
                                    "firstName": "John",
                                    "lastName": "Doe",
                                    "travelerID": ["2005CCE0000359CA"],
                                },
                            }
                        },
                    }
                ],
                "originAirportCode": "DEN",
                "destinationAirportCode": "PHX",
                "flightNumber": "3556",
                "hasWifi": True,
                "travelTime": "1h 55m",
            }
        ],
        "_links": {
            "checkInSessionToken": "eyJwbnIiOnsiY29uZmlybWF0aW9uTnVtYmVyIjoiTVI2RDZOIiwicGFzc2VuZ2VycyI6WyJNaWNoYWVsIFRldGxvdyJdLCJwYXNzZW5nZXJzTmFtZXMiOlt7ImZpcnN0TmFtZSI6Ik1JQ0hBRUwiLCJsYXN0TmFtZSI6IlRFVExPVyJ9XX0sImNhcmRzIjpbeyJkYXRlcyI6eyJmaXJzdCI6IjIwMTktMTAtMjAifSwiZGVzdGluYXRpb25EZXNjcmlwdGlvbiI6IlBob2VuaXgiLCJkZXBhcnR1cmVEYXRlIjoiMjAxOS0xMC0yMCIsImRlcGFydHVyZUFpcnBvcnQiOiJERU4iLCJkZXBhcnR1cmVUaW1lIjoiMTI6MjUiLCJhcnJpdmFsQWlycG9ydCI6IlBIWCIsImFycml2YWxUaW1lIjoiMTM6MjAiLCJmbGlnaHRzIjpbeyJmbGlnaHROdW1iZXIiOiIzNTU2IiwiaGFzV2lmaSI6dHJ1ZSwidHJhdmVsVGltZSI6IjFoIDU1bSIsImFxcVN0YXR1cyI6IlRTQV9QUkVfQ0hFQ0siLCJvcmlnaW5BaXJwb3J0Q29kZSI6IkRFTiIsImRlc3RpbmF0aW9uQWlycG9ydENvZGUiOiJQSFgiLCJkZXN0aW5hdGlvblN0YXRpb25OYW1lIjoiUGhvZW5peCIsImRlcGFydHVyZURhdGUiOiJPY3QgMjAiLCJkZXBhcnR1cmVHYXRlIjoiQzQ5IiwiZGVwYXJ0dXJlVGltZSI6IjEyOjI1In1dLCJ0cmF2ZWxUaW1lIjoiMWggNTVtIiwiaW50ZXJuYXRpb25hbCI6ZmFsc2V9XSwiYWlyVHJhdmVsVG9rZW4iOiJleUpoYkdjaU9pSmthWElpTENKbGJtTWlPaUpCTVRJNFEwSkRMVWhUTWpVMkluMC4ud2tMWkxtWTBMYnk2SGZEQkljaG1qZy5CckxHR01xdXBqZGI2QlpneDhlY0VHWUdhVy1xMHAtLS0zVTNTdWVuSkx3dmdjNzV0aGE4ZVBydm5wT3BLbTJsblZ5UWZvVnNfSk1yTkNsRENNSUxyWTY5ZHVKekloa0N2a0xUb3d4OVo2N2Q4eGItVW1acHoyZlh5QTIzV1E3RGdsTFpxUnlsSmtsRmZ3aTJvNW1TMGxsNzl6Ukpxb2ExMjJOdUs3Q3lPWFRYNUE1XzJraThZWnRzbDZWY1h3Zk91eEhBZUhFaTRnWXYyc1oyaHBzYm9jZHp1YXFaeHdFTWNQXzBNQ1dzaVBKNEhpMFc5dkRkY2VNRVA3Vmc4RzhTdUNydV9nSWFWcnlGOEpxZVlmZlZjV3FtNEM4b1ZJZnBmdXotMndIVjZMazV2WWhRQTE1bGRIRU5CdXdXVVpsUVNycnZTaHFaZTFxSWJRNkNyQWxyZENjTFo3MlRxdm0wcjR1MnFGSGw3V3FqQ01PREtrT2ROUzVwTkpFWUE1V1V4VXNkWjNvN3F4Z0RhbWZjXzNMNE1ZOVFKQXZ4N0djbzQ4U09jRjBLaDVwbGpiVGhxZTVOMHQyRFdvUGpoSU5waWNMLU00eE9TVHB6b2REeGczdlJQQmxPN0tkemNPR3lNMjVHZ1R4X2w1MG5yNWZQQ0FFUlN2OUYtZlpFNUZ6TDQ4RENfdG9rQjNRWUM5emZ0b1lfM2ZQcFNvRy04bFVLZEhqdmxrQ3lHUVR6Q0J2MGJzUEoxRGF6b3Jibm1SN0theUFrdHJQNmdXU1NsaUpFNHJTWWpRUXVmV193YlJJRFFhRkFTTnR2TW92UTdMUWtGR0UwaEJrSmNBRU9DckhESjNObzRMSjM5aGswSldUVWlGNmZXbUNBRW9zalhkOS1qaEtzc1JDLXJWckw5VC1kMkVLQjVDeGtTbjhqVjU3cWI4dkVFX1Y5TGRkbnNHWGpXaXVqdkRPTWpGSm5YV19QMlltTUdKdS1YS3REOWpVV3BYZGFzdEFKVEpqbXlvNDBDcFN0TEQ1VVpRTmZUTS1fSUFGMDN2UDhrQVhjMTBURWRQWnJsR0xtaEVFdl9QaV9QUHBsbms4YW5CSDhPeE5yazBBTGpEOGRKZGdjcFNvMHdlajBodE40a0hKR2dfTjZsaVRCMVVGQ04yWVJCcjUxR2xRNVpxUDBKUWxUT2Q0WFlJSkxNSldhMFFaNnRnQnNId1ZSNXZ6Z3dUaENjYm9wUU5rbzhOM25KeWVhZHFuSkFEcFpvcWxFN0ZEdGVhUXFXejdHN3FiU0RFNWh0TXZXSV9DeGZHS0ltWFQ1X3YzUUtWWlN5NndkNk4tSTVpMkZtUGJNajRVZmhySEdrcU9pcnpSQThWNTNPOW1jMF9lTWVKR0RBWElPQk15MDF1WVlfUDRGb3VKNExfUUxDYkxsX3lpRzlONW9OZU9Jc3Axc3BiRk83UEdMOTFEUFdaOU9sblBTelMtakRWcEY1V1VwZVVlSGZQSlJmU2FuVXR5TkRkTUNhU3RUbXR1cnVfNE9pYlF2dy00cUJZT29NWjlIRnFReTIzRVhtbjhUQzJVUkE3VEI2ZEpVdnhiYW9BU0FFcXEzT1RZNTRwal94TkpQTHJKYWswUVNvU0FEWXhoSW1FTmNZSGpybkNyNEhOVHJwYk04a2hpd2xIX0RLeVUwM1h0MEVoZzRUQktJLVhnZzZrQm9ZTVBPNWx5N09zbm5KSm83dzZPMjBLR2FjQWNtUHNSa0ZKc0hVcHFvVTk3bHI0OWVWeTNHM1YybjhTbVREVEkzLUJqRzFtdDBLV3JRVTRlcG9BQnRzYzNOS0JJcXdPVUJwZ1dFNU5lVmJmMXlydWxMQklTSUhPVzhKeTJIdFVYV1VtSWdHMThPRnJ2cXBYYURldmtVejlpTVV6SkEyaU9wcDBCNDFQdUNlMFFxSWFvRk81NHJSX251eTR0UEM0RlNWU0gtZVRLNWpkSGdHVUJ2T1Rta3ZNUlNFeTRZamxkMzJQN2FRb0F4aFVTY3RrbjVIZ0hmcU5HczQ3Uk5PQTFaQ0hLVmw0X25fZmYwd2o4S0czVE5KUVZWaEFoSXp6cDlMZmlnak5aTVFCaTM0eXoyQnY4SE9hMGZZVEdENHpXX1BjZFQtZ1dVZlJrNzBNTEFOYllYZ2praUR3LTJ1cV9rU2xuYlN4eUYtUzdyUmsxWFZ2VkRCZUVNOWhJdFFENVhVMFR5UlVLZVFKSk5TanZEeFNXcFA5MVA1OWkwbElqTFh3U2xVRUZWRTdhYTlqd0RCT1c0eWRNSmx5NDhiaVlzOWdfMndIWFRoR0hPRl9kbXRmYkttc2JNX1o5TlJtdHZwbVJUSjZDdHhRNUVTV0hFYm5qeWUxaTBlMUpHczdCMVhsUndsVm8zNVg5S0lIT0xHSDNoQWlwLVZmalVtbk5ycnVzRXhic1AwYjFLdkQwU2k2MHl1TUhBdzhXLXRzSFRnUTJBSzlXdG1JT0p1Q3lCbFEwQzFoajdXSDFBdUhScUNCUHJSUGdRbExadFdyX0d3bFg1S29XcW9wdVdTZHRJYXJGS2d0X2duTHNGay1TYlBWR1FodW0wZWk0UmRBMjYzcmtqZk5jLTFBbldRcDM3M28yVkI4M1JQdXVFVEJMcks0Yy1yeUh1YUlzRnNmeFlZRGtGc2ZEVE5UVXk1ejluX2E0QVI4TVc3Mko5Y2FSOWhhZFdOQ2hRak1wVks5STBmZkFZSDFKYkN5S3FMT190UmVkcnVzRnFsQXNmQV9CTTd0NjJucnlHdG1tdGdHelBrd0lFNTdWako1MFNFMS1HNjMwYUx4QlhBMDM1b3hEcDh1Tk5VUVdRVTdNMDI2NlRZQXl5M1BjbUxiai05QUNGTktlSXdJaXZCZ09Uc1U3NHRPRVphTTN3djZELWxEVjJQcEplZ3NIZWc2eEZRcndZVmw5V0F1REdSV2FvUm1EeHdlc19FcmtGdWRxclVCdmxLSGpXTGhZd2l2cW55QVRfOUh1bWhORFVVRU1fVWZZWUl4d09PS29iWWVySTRLeXpsRUlad3BFWFhZY2JaNTVSa3dLYk9vM1VIV2tObldVTmp1ZXpJQnVrSjNIdXF1ZmdVc2lpbUkyWGUtb0tFc2tYSFAtNDc5U3VoWTJCWU9HTnJEeG95WXJjQ25hTjREOHdkM0t0VGo5Nm9zc2hpZWt4cXlNc2dndFlaU1NTTlZ4VGRwZWF2cEFmNENpaEdKR1JaZW90YVB0T1NIaDVDNUx3WkM5LWFBaWFOZXcwRlZkMFBnX1J4Yi1MWVVQZ1NrU2oxNFJJTnhrczliNGZOWmd2anNNZVFiRkhVZW9PVTVpR3V4Q0NsbnFEaFBsTmJ0MjM2YTlpSV9ZRnhoYnY5Sk5qOWVJb3lQUUZ2MFRPVU1QcUc5ejdHbnhicWQxV2xzREFjeEdScS12NThBRzJ0MF9ndFA4eXFpY2M3RGV3bmVkTFItOU1KcGJGTWdwU2hDRTJ4QXRnU1pnbjJYRXFTQUZKdG5YdW51VWhXQnMxZDhsYmk4OVNYUVBPMGx3N201N1pWYVlRbHJHd1NtUy1rUC1FaktEZ0s4OEdib0F5NDhiR2FsQUpqMGZ4NEFRY3FsT0lzU1A0dDV4RURHejNNcHFsLUN4WmwwQWNFRUpJTDdfRVNKNFhnbHp4ZzZIakRxbklpbmRWLUR0bWVrZkZpQ2ctdGNFWWFISW0ySXBWbFgtcTNoR2VXUGpIWF91cG0yVWN3N0ZUMkNaWWhmYTZsMll1bm1wSW5TVVBGMGhBREthdGFQVWRkbVI2NHMyaDlzNWpEOTN4bkZaYWs2V3B3Y0V2LTgwc240YnNGY25xNHhVY0ZUREYwQnA1aWxwMDhOdksxTVFhUG9zVWZVRExHYnFfSzJoLXBIVjg1dDh4WFVNbTJwLWdydFY1bWRENVJHa1gwc1R4SmVWaEQzUE9sMTlueldTdWJfTUNlRVNlLTB3dFdtd0lNMFBscGk1Mzhub0pTdGJqdFZpYVY1MnVwcTNlclo4TG05d0N6LU1QSzRURE4zamF4SFUwaUtFN0hudE4yeVh1Ym12bnpCQV81NUJJN3p5VlhhMEF1REdINmNVZ2t6NE9UTzhDNktUMEpCeFM4ajA5UE02WEEtVUhmZ1gwV0dnT1VlSnBtZjgxeTVmVVRVX3F0dG9NNUdXRmtLQlVWc3hxQmx6N0hMSnU0QVNyQmFaZEcwS204MW9qUmJSc2Nidy1PQVltNW55QUE1QW90NlRlWTRvVmJONU9xWDlRS0loLTlCQ3dzcmtuaV9RX0x3U00zb3pWZWItRVF1emQzSXVGWTlHUElPcDIzM1lDRlNXcl81dkhnalJXTVhRSG1FQ29jZ05Pb1VoRUYtNnhmdEFvT0JpeGljdGFxVkdqSzlucXdWOVJaSmZ5TjVoY3Utd0hnYmNLVDZvdXdkcUxEbkQ2S3JJd1lYZVROUmhzMlZVZ1lLNzV1MXBYcDc5RU0wSmh0TDg5RGw3dkVqX21qbmZyNE9YTHZTaG9nS2V4WEJ5enlLMHZEWDFpdGsyZnFPYmNRb2ptamUyRDNSdmFnWFl6TTBXM2oxZy15Vm14VGwwR0M5eG1jQmZtZjJLcUttNk05Y0NzNzRUemNnSmRGOE5IZUpuTmphenRWSVVXMkJUQXZVVE5CbWRWcEUwSzZzclpxNFpTRmI2d3pQOV9mWmdRSTFpSnhmeEo4WnhwRW9EeVJjMHotTlJkTldVeGV4V0U4ckdLTHE2MG44ZTREV0E2YWpDLXdOVzNia0N5Y3RzVkpQUGJla3RuTW9wM1IzR1VNdGNFSzVHWGdZbElsbGxsY1Z5WHZTUFg1Wm03RVpBREgydm5vOVZ2MFNMSmxzNFlsYUIya2FobFJ1ZklVbW9QZGhpdnBkMVRXblhNM1ZheUs5OE45bGx0UHlVTllSa0FFS1gyNDc1bFZNSGVsem1ERDMxdW5xdVJoTktxVWxqT19IQldqRkVmanItLXoteC1FOVF4OVQ0MHlvelJhU000UFBWNk5JcHZpMW1SaEZQNDJ6MVhUb1ljVnpXTHV4WFhCRE84QUFndnI2SlphRWlrZVUwVENYNHVDMGtKMU9VTHFLQmF0SExBRlJxU1lIcFVybUF4elpBUV9oWGF6ZDlqY2RvNml0WnpuMXZkTmpqeHBYTllVem1aQjdSa3cxblpOZlU4bzZhcV8zTk5PdjA2enBQaWt2UGFydkM3bUxtR1NlYm9adzZRM3JIazkwR0YxZjd4em43d0lYOGhRVTU1MUJuWWd5a0pmQk5FdGV4SlJuMDV3REYwWXAyWDIyNmhZT1dfOGZ1QmtSZXAyY1NqTDBGVnV1Rl96cnA0VmJPY3pWcm9rbGVTdklxYUM5d3hXck5BQ1ZuSkUxTW5hSUw5YzhtYmEtdFNBTExFbDktZ05DU2szenZNN3JIRENiSlZmclY5MG9nbGppMmVpYTgxVm9kTDYydVE0V0k5VWtWa19ab01OekJ5X3hoMW43NFBUUkVvYVNNZnJSVjNjcVdTVk9KVDFxOUtLSWwxYlR4NmM3NjlnSXFLUTNYTC1JOXRYbm91RDVfemNaRktZUjYyVHU1WUJPa2U5MjFlaDdxY29IUzhSbmlseFpaTDhIamtFcWxzZ0dJS0hYSnBjbkVuNTUtMndRMzZzZjdrNzNwaUhEVU5QYTZ5YkZBbkRZV3Byakl3V3ZvNWt3VEhWaWRoUzV6MmpCVDZoSThMMVNNbVhmdC1XMjNFSU5PLWtMWmxHcVFKOUlINENHYllZVXVIMXNOeXMxVTV0dEYwUEJaVUlDTmJ3LUJjbUZqWHpBcnhJT2FNUDJjNUZYdjE0LXZjUGE4NXE2WV9VREtsUFBWSE91dm9tXzJtRVZiWmQ5aHZpVGNjMnFPSGhQXzJzZXFOejMyYXZxSUVsWnFpbFVWd0FjQUx6dmFhWEVjY2owSTZuQjFSbTBCcjdGR2NQQnZnWVQ5OHVhSVZsRFB5MWF3MWF5QVhtWFVVajRCX0FCSXFMSkNHMG9uOF9LZmhfd3dXYWNuX0E0a3lVS09qQnpZdjZSVVU1VHViWVlXZVZrNHQ2bW9vUGhrQnM2NVUyeVl1QVNlZkZ4Nlc1Q1N6VjRGd0lFTzJUTkFjVks0ZUJPTXJldFMwNXpBcUR2UVFteXNHeEE4aGRrei04R1o5cnE0SlpTaGVXQ09EcEI4T3NuNHY2M3MxZ3dCMFNXYkNGMkdmOHBqMzdjV2ZKbm11QXk4Rm5KbUtYYlZrNkpFTzdZUGpUcTc1QS1QaFNHUTU2Q2NELVp4MHJUSXRZSE9LRVNTb1Jub1dNcjBTVmZfaVhOdjFBVWR1bzRBakdmT3l5M05JR3RMZ25VOWEteTV1M3ZBcTZGZllBd05femVRZVRBMVphZGNrQ1c3U0Nab1pWeFpjN2hadldqZk5XdzRXT0wtQjI5Q2xkNUREODJDWDVqRWVodkhSR2VfcElhNDZCTVhSTTJKUENxcVBWMDctSC1nQjFkV3Vzckk4NVMwQ1RjMFFyZzFMMHJQblJFYkgzVFN5S1pXR0YzUTZ1SXNIUTdpeGllaWtTRHBWTHJIUzFjUmFoT3ZXU1psWXBHUU9hQnJ4TG91VHNnQ0FDdjhFeGtuMjF1bkRNbTFkTEkxZDlXTnZodkdoMG5wMURxSmJBd0dzMVdTX0NIMmh5MkFibDhRdjBiYlN6eE5xLnNuVVFTUzZOWmhZcDh0Q2YtZ05mYlEiLCJfbGlua3MiOnsidHJhdmVsRG9jdW1lbnRzIjpbeyJib2R5Ijp7InJlY29yZExvY2F0b3IiOiJNUjZENk4iLCJ0cmF2ZWxlcklkZW50aWZpZXIiOiIyMDA1Q0NFMDAwMDM1OUNBIiwiZmlyc3ROYW1lIjoiTUlDSEFFTCIsImxhc3ROYW1lIjoiVEVUTE9XIiwiZnVsbE5hbWUiOiJNaWNoYWVsIFRldGxvdyIsImFjY291bnROdW1iZXIiOiI2MTUyMDU2NjIiLCJlbGlnaWJsZUZvckRyaW5rQ291cG9uIjpmYWxzZSwicGFzc2VuZ2VyVHlwZSI6IkEifSwiYm9hcmRpbmdCb3VuZHMiOlt7ImluZGV4IjoxLCJib2FyZGluZ1NlZ21lbnRzIjpbeyJ0cmF2ZWxlclNlZ21lbnRJZGVudGlmaWVyIjoiMjAwMDFDRTAwMDE0QjExNyIsImVsZWdpYmxlRm9yRHJpbmtDb3Vwb24iOmZhbHNlLCJib2FyZGluZ0RldGFpbHMiOnsiY3VzdG9tZXJBY2NlcHRhbmNlU3RhdHVzIjoiTk9UX0FDQ0VQVEVEIiwic2VnbWVudFN0YXR1cyI6eyJnZW5lcmFsU3RhdHVzIjoiT1BFTiJ9fSwiaGFzVHNhUHJlY2hlY2siOnRydWUsInZhbGlkQXFxU3RhdHVzIjp0cnVlLCJzZWdtZW50Qm9va2luZ1N0YXR1cyI6IkNPTkZJUk1FRCJ9XX1dfV19fQ==",
            "viewBoardingPassIssuance": {
                "href": "/v1/mobile-air-operations/page/check-in/retrieve-boarding-pass/MR6D6N",
                "method": "POST",
                "body": {
                    "firstName": "John",
                    "lastName": "Doe",
                    "travelerID": ["2005CCE0000359CA"],
                },
            },
            "viewAllBoardingPasses": None,
        },
    }
}
