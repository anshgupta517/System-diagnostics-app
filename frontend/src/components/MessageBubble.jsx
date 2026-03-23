import React from 'react';
import ReactMarkdown from 'react-markdown';
import DataVisualizer from './DataVisualizer';

const MessageBubble = ({ role, content, data }) => {
    const isUser = role === 'user';

    return (
        <div className={`flex w-full mb-4 ${isUser ? 'justify-end' : 'justify-start'}`}>
            <div
                className={`max-w-[80%] rounded-2xl px-5 py-5 ${isUser
                        ? 'bg-blue-600 text-white rounded-br-none'
                        : 'bg-zinc-800 text-gray-100 rounded-bl-none border border-zinc-700'
                    }`}
            >
                <div className="text-sm">
                    {isUser ? (
                        <p className="whitespace-pre-wrap leading-relaxed">{content}</p>
                    ) : (
                        <ReactMarkdown 
                            components={{
                                p: ({node, ...props}) => <p className="mb-3 last:mb-0 leading-relaxed" {...props} />,
                                strong: ({node, ...props}) => <strong className="font-bold text-white" {...props} />,
                                ul: ({node, ...props}) => <ul className="list-disc list-inside mb-3 space-y-1" {...props} />,
                                ol: ({node, ...props}) => <ol className="list-decimal list-inside mb-3 space-y-1" {...props} />,
                                li: ({node, ...props}) => <li className="text-zinc-200" {...props} />,
                                code: ({node, inline, ...props}) => 
                                    inline 
                                    ? <code className="bg-zinc-900 px-1 py-0.5 rounded text-blue-300 text-xs font-mono" {...props} />
                                    : <pre className="bg-zinc-950 p-3 rounded-lg overflow-x-auto mb-3"><code className="text-blue-300 text-xs font-mono" {...props} /></pre>
                            }}
                        >
                            {content}
                        </ReactMarkdown>
                    )}
                </div>
                {!isUser && data && <DataVisualizer data={data} />}
            </div>
        </div>
    );
};

export default MessageBubble;
