type ChatContainerProps = {
  children: React.ReactNode
}

export function ChatContainer({
  children
}: ChatContainerProps) {
  return (
    <main
      style={{
        width: "100%",
        minHeight: "100vh",
        background:
          "linear-gradient(135deg, #eef2ff 0%, #fdf2f8 48%, #ecfeff 100%)",
        display: "flex",
        justifyContent: "center",
        alignItems: "center",
        padding: "24px"
      }}
    >
      <div
        style={{
          width: "100%",
          maxWidth: "1400px",
          height: "94vh",
          background:
            "linear-gradient(180deg, rgba(255,255,255,0.96) 0%, rgba(250,245,255,0.9) 58%, rgba(236,254,255,0.92) 100%)",
          borderRadius: "32px",
          position: "relative",
          overflow: "hidden",
          display: "flex",
          flexDirection: "column",
          padding: "32px",
          border: "1px solid rgba(255,255,255,0.72)",
          boxShadow:
            "0 24px 70px rgba(79,70,229,0.18)"
        }}
      >
        {children}
      </div>
    </main>
  )
}
