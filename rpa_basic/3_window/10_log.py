import logging
logging.basicConfig(level=logging.DEBUG,format="%(asctime)s [%(levelname)s] %(message)s" ) ## 시간정보가 나오는거임


logging.debug("아 이거 누가 짠거야~~")


logging.info("자동화 수행 준비")
logging.warn("이 스크립트는 조금 오래 되었습니다. 실행상 문제가 있을수도 있어요")

logging.error("에러가 발생하였습니다. 에러 코드는 ...")