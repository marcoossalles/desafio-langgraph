type ChatHeaderProps = {
  title: string
}

export function ChatHeader({
  title
}: ChatHeaderProps) {
  return (
    <div
      style={{
        flex: 1,
        display: "flex",
        justifyContent: "center",
        alignItems: "center",
        flexDirection: "column",
        textAlign: "center",
        zIndex: 2
      }}
    >
      <div
        style={{
          fontSize: "36px",
          marginBottom: "24px"
        }}
      >
        ✦
      </div>

      <h1
        style={{
          fontSize: "42px",
          fontWeight: 400,
          color: "#111827",
          maxWidth: "760px",
          lineHeight: 1.2,
          letterSpacing: "-1px"
        }}
      >
        {title}
      </h1>
    </div>
  )
}