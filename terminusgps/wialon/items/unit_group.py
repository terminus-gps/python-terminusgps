from terminusgps.wialon import flags
from terminusgps.wialon.items.base import WialonBase


class WialonUnitGroup(WialonBase):
    def create(self, **kwargs) -> int | None:
        if not kwargs.get("owner_id"):
            raise ValueError("'owner_id' is required on creation.")
        if not kwargs.get("name"):
            raise ValueError("'name' is required on creation.")

        response = self.session.wialon_api.core_create_unit_group(
            **{
                "creatorId": kwargs["owner_id"],
                "name": kwargs["name"],
                "dataFlags": flags.DATAFLAG_UNIT_BASE,
            }
        )
        return response.get("item", {}).get("id")
