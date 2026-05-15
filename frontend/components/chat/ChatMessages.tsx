"use client"

import {
  useEffect,
  useRef
} from "react"

import { ChatMessage } from "./ChatMessage"

type Message = {
  role: "user" | "assistant"
  content: string
}

type ChatMessagesProps = {
  messages: Message[]
  loading: boolean
}

export function ChatMessages({
  messages,
  loading
}: ChatMessagesProps) {
  const messagesEndRef =
    useRef<HTMLDivElement | null>(null)

  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({
      behavior: "smooth"
    })
  }, [messages, loading])

  return (
    <div
      style={{
        flex: 1,
        minHeight: 0,
        width: "100%",
        overflowY: "auto",
        padding: "24px 0",
        position: "relative",
        zIndex: 2
      }}
    >
      {messages.map((msg, index) => (
        <ChatMessage
          key={index}
          role={msg.role}
          content={msg.content}
        />
      ))}

      {loading && (
        <div
          style={{
            marginBottom: "20px"
          }}
        >
          <div
            style={{
              display: "inline-block",
              padding: "14px 18px",
              borderRadius: "20px",
              background: "#f3f4f6",
              color: "#6b7280",
              fontSize: "14px"
            }}
          >
            ✨ AI Movie está digitando...
          </div>
        </div>
      )}

      <div ref={messagesEndRef} />
    </div>
  )
}
