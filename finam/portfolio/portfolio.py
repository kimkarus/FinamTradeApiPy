from typing import Union

from finam.base_client.base import BaseClient
from finam.models import ErrorBodyModel
from finam.portfolio.model import PortfolioRequestModel, PortfolioResponseModel


class PortfolioClient(BaseClient):
    def __init__(self, token: str):
        super().__init__(token)
        self._portfolio_url = "/api/v1/portfolio"

    async def get_portfolio(self, params: PortfolioRequestModel) -> Union[PortfolioResponseModel, ErrorBodyModel]:
        params = {
            "clientId": params.clientId,
            "content.IncludeCurrencies": params.includeCurrencies,
            "content.IncludeMoney": params.includeMoney,
            "content.IncludePositions": params.includePositions,
            "content.IncludeMaxBuySell": params.includeMaxBuySell,
        }
        response, ok = await self._exec_request(self.RequestMethod.GET, self._portfolio_url, params=params)
        if not ok:
            return ErrorBodyModel(**response)
        return PortfolioResponseModel(**response)
