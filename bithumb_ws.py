import asyncio
import websockets
import json

# 빗썸 WebSocket 주소
BITHUMB_WS_URL = "wss://pubwss.bithumb.com/pub/ws"

async def subscribe():
    async with websockets.connect(BITHUMB_WS_URL) as websocket:
        # 구독 요청 (BTC/KRW 실시간 체결 정보)
        subscribe_msg = {
            "type": "transaction",
            "symbols": ["BTC_KRW"]
        }
        await websocket.send(json.dumps(subscribe_msg))
        print("✅ 빗썸 WebSocket 구독 시작...")

        # 실시간 데이터 수신
        while True:
            response = await websocket.recv()
            data = json.loads(response)
            print("📩 실시간 데이터:", data)

# 비동기 실행
asyncio.run(subscribe())
# 이 코드는 빗썸의 WebSocket API를 사용하여 BTC/KRW의 실시간 체결 정보를 구독합니다.
# 구독 요청을 보내고, 실시간으로 수신되는 데이터를 출력합니다.
# 이 코드를 실행하기 위해서는 websockets 라이브러리가 필요합니다.
# pip install websockets
# 이 코드는 Python 3.7 이상에서 실행되어야 합니다.
# asyncio를 사용하여 비동기적으로 WebSocket에 연결하고 데이터를 수신합니다.
# 빗썸 API 문서: https://docs.bithumb.com
# 빗썸 WebSocket API 문서: https://docs.bithumb.com
