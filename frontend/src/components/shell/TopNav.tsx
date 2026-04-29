import GlobalSearch from "./GlobalSearch";
import NewRunButton from "./NewRunButton";
import PrimaryNav from "./PrimaryNav";
import UserMenu from "./UserMenu";
import WorkspaceSwitcher from "./WorkspaceSwitcher";

export default function TopNav() {
  return (
    <header
      className="sticky top-0 z-40 surface-ink"
      style={{ borderRadius: 0 }}
    >
      <div className="mx-auto flex h-14 items-center gap-4 px-6 max-w-[1600px]">
        <div className="flex items-center gap-3 shrink-0">
          <WorkspaceSwitcher />
        </div>

        <div className="flex-1 flex justify-center">
          <PrimaryNav />
        </div>

        <div className="flex items-center gap-3 shrink-0">
          <GlobalSearch />
          <NewRunButton />
          <UserMenu />
        </div>
      </div>
    </header>
  );
}
