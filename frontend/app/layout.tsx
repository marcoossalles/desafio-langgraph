import type { Metadata } from "next"
import type { ReactNode } from "react"

export const metadata: Metadata = {
  title: "Movie Chatbot",
  description: "AI movie recommendation chat"
}

type RootLayoutProps = {
  children: ReactNode
}

export default function RootLayout({
  children
}: RootLayoutProps) {
  return (
    <html lang="pt-BR">
      <body
        style={{
          margin: 0,
          fontFamily:
            "Arial, Helvetica, sans-serif"
        }}
      >
        {children}
      </body>
    </html>
  )
}
