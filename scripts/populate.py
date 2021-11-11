from octoauth.architecture.database import DBModel
from octoauth.domain.accounts.services import AccountService, AccountCreateDTO
from octoauth.domain.oauth2.dtos import ScopeDTO
from octoauth.domain.oauth2.services import ApplicationService, ApplicationCreateDTO, ScopeService

DBModel.metadata.drop_all()
DBModel.metadata.create_all()


AccountService.create(AccountCreateDTO(
    username="hoshiyosan",
    email="sledeunf@gmail.com",
    password="démo",
    profile_url="https://m.media-amazon.com/images/I/71hZpyFFp0L._SS500_.jpg"
))

ApplicationService.create(ApplicationCreateDTO(
    name="Sortify",
    description="An application to sort your playlists in the Cloud.",
    client_id="sortify",
    icon_uri="https://cdn-icons-png.flaticon.com/512/2111/2111624.png"
))

ApplicationService.create(ApplicationCreateDTO(
    name="OctoAuth",
    description="Account managements for Sortify.",
    client_id="octoauth",
    icon_uri="https://account.sortify.local/octoauth.png"
))

ScopeService.create(ScopeDTO(
    code="groups:read",
    description="View your OctoAuth groups."
))

ScopeService.create(ScopeDTO(
    code="profile:read",
    description="Update information from your profile."
))

ScopeService.create(ScopeDTO(
    code="groups:edit",
    description="Edit your OctoAuth groups."
))