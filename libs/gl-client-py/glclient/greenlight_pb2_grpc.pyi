"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import abc
import collections.abc
import greenlight_pb2
import grpc

class NodeStub:
    """The node service represents your node running on greenlight's
    infrastructure. You can use the exposed RPC methods to interact
    with your node. The URI used to connect to the node depends on
    where the node is being scheduled and is returned by the
    `Scheduler.Schedule()` RPC call.

    Notice that in order to connect to the node the caller must use the
    node-specific mTLS keypair returned by `Scheduler.Register()` or
    `Scheduler.Recover()`. In particular the anonymous mTLS keypair is
    rejected by the node.
    """

    def __init__(self, channel: grpc.Channel) -> None: ...
    GetInfo: grpc.UnaryUnaryMultiCallable[
        greenlight_pb2.GetInfoRequest,
        greenlight_pb2.GetInfoResponse,
    ]
    """Retrieve general information about the node."""
    Stop: grpc.UnaryUnaryMultiCallable[
        greenlight_pb2.StopRequest,
        greenlight_pb2.StopResponse,
    ]
    """The stop is a RPC command to shut off the c-lightning node"""
    ConnectPeer: grpc.UnaryUnaryMultiCallable[
        greenlight_pb2.ConnectRequest,
        greenlight_pb2.ConnectResponse,
    ]
    """Connect to a node in the network. (`Connect` alone clashes
    with tonic internals).
    """
    ListPeers: grpc.UnaryUnaryMultiCallable[
        greenlight_pb2.ListPeersRequest,
        greenlight_pb2.ListPeersResponse,
    ]
    Disconnect: grpc.UnaryUnaryMultiCallable[
        greenlight_pb2.DisconnectRequest,
        greenlight_pb2.DisconnectResponse,
    ]
    """The disconnect RPC command closes an existing connection to
    a peer, identified by node_id, in the Lightning Network, as long
    as it doesn't have an active channel. If force is set then
    it will disconnect even with an active channel.
    """
    NewAddr: grpc.UnaryUnaryMultiCallable[
        greenlight_pb2.NewAddrRequest,
        greenlight_pb2.NewAddrResponse,
    ]
    """The newaddr RPC command generates a new address which can
    subsequently be used to fund channels managed by the
    c-lightning node.
    """
    ListFunds: grpc.UnaryUnaryMultiCallable[
        greenlight_pb2.ListFundsRequest,
        greenlight_pb2.ListFundsResponse,
    ]
    """Retrieve a list of funds managed by this node.

    This includes both on-chain funds and off-chain
    funds. Off-chain funds are bound to a channel, and we
    consider only the balance that is currently spendable by
    the node, i.e., we do not return the full channel's
    capacity, just the balance that belongs to this node.

    The on-chain funds correspond to outputs that the wallet
    can spend.
    """
    Withdraw: grpc.UnaryUnaryMultiCallable[
        greenlight_pb2.WithdrawRequest,
        greenlight_pb2.WithdrawResponse,
    ]
    FundChannel: grpc.UnaryUnaryMultiCallable[
        greenlight_pb2.FundChannelRequest,
        greenlight_pb2.FundChannelResponse,
    ]
    CloseChannel: grpc.UnaryUnaryMultiCallable[
        greenlight_pb2.CloseChannelRequest,
        greenlight_pb2.CloseChannelResponse,
    ]
    CreateInvoice: grpc.UnaryUnaryMultiCallable[
        greenlight_pb2.InvoiceRequest,
        greenlight_pb2.Invoice,
    ]
    """Create a new invoice to receive an incoming payment."""
    Pay: grpc.UnaryUnaryMultiCallable[
        greenlight_pb2.PayRequest,
        greenlight_pb2.Payment,
    ]
    Keysend: grpc.UnaryUnaryMultiCallable[
        greenlight_pb2.KeysendRequest,
        greenlight_pb2.Payment,
    ]
    """Send a spontaneous payment, optionally with some extra information."""
    ListPayments: grpc.UnaryUnaryMultiCallable[
        greenlight_pb2.ListPaymentsRequest,
        greenlight_pb2.ListPaymentsResponse,
    ]
    """Retrieve a list of payment performed by this node.

    The query can optionally be restricted to a single payment
    matching criteria that can be specified in the
    `ListPaymentsRequest`

    Notice: this does not include any payment that were
    received by this node, just the outgoing payments. Incoming
    payments can be retrieved using `ListInvoices`
    """
    ListInvoices: grpc.UnaryUnaryMultiCallable[
        greenlight_pb2.ListInvoicesRequest,
        greenlight_pb2.ListInvoicesResponse,
    ]
    """Retrieve invoices that were created via CreateInvoice

    The query can optionally be restricted to only return a
    single invoice matching the given criteria.
    """
    StreamIncoming: grpc.UnaryStreamMultiCallable[
        greenlight_pb2.StreamIncomingFilter,
        greenlight_pb2.IncomingPayment,
    ]
    """Stream incoming payments

    Currently includes off-chain payments received matching an
    invoice or spontaneus paymens through keysend.
    """
    StreamLog: grpc.UnaryStreamMultiCallable[
        greenlight_pb2.StreamLogRequest,
        greenlight_pb2.LogEntry,
    ]
    """Stream the logs as they are produced by the node

    Mainly intended for debugging clients by tailing the log as
    they are written on the node. The logs start streaming from
    the first beginning, in order to allow inspection of events
    after an error occurred, That also means that the logs can
    be rather large, and should not be streamed onto
    resource-constrained devices.
    """
    StreamHsmRequests: grpc.UnaryStreamMultiCallable[
        greenlight_pb2.Empty,
        greenlight_pb2.HsmRequest,
    ]
    """////////////////////////////// HSM Messages ////////////////////////

    The following messages are related to communicating HSM
    requests back and forth. Chances are you won't need to
    interact with these at all, unless you want to embed the
    hsmd into your client. We recommend using a standalone hsmd
    such as hagrid, keeper of keys, to get started.

    Stream requests from the node to any key device that can
    respond to them.
    """
    RespondHsmRequest: grpc.UnaryUnaryMultiCallable[
        greenlight_pb2.HsmResponse,
        greenlight_pb2.Empty,
    ]

class NodeServicer(metaclass=abc.ABCMeta):
    """The node service represents your node running on greenlight's
    infrastructure. You can use the exposed RPC methods to interact
    with your node. The URI used to connect to the node depends on
    where the node is being scheduled and is returned by the
    `Scheduler.Schedule()` RPC call.

    Notice that in order to connect to the node the caller must use the
    node-specific mTLS keypair returned by `Scheduler.Register()` or
    `Scheduler.Recover()`. In particular the anonymous mTLS keypair is
    rejected by the node.
    """

    @abc.abstractmethod
    def GetInfo(
        self,
        request: greenlight_pb2.GetInfoRequest,
        context: grpc.ServicerContext,
    ) -> greenlight_pb2.GetInfoResponse:
        """Retrieve general information about the node."""
    @abc.abstractmethod
    def Stop(
        self,
        request: greenlight_pb2.StopRequest,
        context: grpc.ServicerContext,
    ) -> greenlight_pb2.StopResponse:
        """The stop is a RPC command to shut off the c-lightning node"""
    @abc.abstractmethod
    def ConnectPeer(
        self,
        request: greenlight_pb2.ConnectRequest,
        context: grpc.ServicerContext,
    ) -> greenlight_pb2.ConnectResponse:
        """Connect to a node in the network. (`Connect` alone clashes
        with tonic internals).
        """
    @abc.abstractmethod
    def ListPeers(
        self,
        request: greenlight_pb2.ListPeersRequest,
        context: grpc.ServicerContext,
    ) -> greenlight_pb2.ListPeersResponse: ...
    @abc.abstractmethod
    def Disconnect(
        self,
        request: greenlight_pb2.DisconnectRequest,
        context: grpc.ServicerContext,
    ) -> greenlight_pb2.DisconnectResponse:
        """The disconnect RPC command closes an existing connection to
        a peer, identified by node_id, in the Lightning Network, as long
        as it doesn't have an active channel. If force is set then
        it will disconnect even with an active channel.
        """
    @abc.abstractmethod
    def NewAddr(
        self,
        request: greenlight_pb2.NewAddrRequest,
        context: grpc.ServicerContext,
    ) -> greenlight_pb2.NewAddrResponse:
        """The newaddr RPC command generates a new address which can
        subsequently be used to fund channels managed by the
        c-lightning node.
        """
    @abc.abstractmethod
    def ListFunds(
        self,
        request: greenlight_pb2.ListFundsRequest,
        context: grpc.ServicerContext,
    ) -> greenlight_pb2.ListFundsResponse:
        """Retrieve a list of funds managed by this node.

        This includes both on-chain funds and off-chain
        funds. Off-chain funds are bound to a channel, and we
        consider only the balance that is currently spendable by
        the node, i.e., we do not return the full channel's
        capacity, just the balance that belongs to this node.

        The on-chain funds correspond to outputs that the wallet
        can spend.
        """
    @abc.abstractmethod
    def Withdraw(
        self,
        request: greenlight_pb2.WithdrawRequest,
        context: grpc.ServicerContext,
    ) -> greenlight_pb2.WithdrawResponse: ...
    @abc.abstractmethod
    def FundChannel(
        self,
        request: greenlight_pb2.FundChannelRequest,
        context: grpc.ServicerContext,
    ) -> greenlight_pb2.FundChannelResponse: ...
    @abc.abstractmethod
    def CloseChannel(
        self,
        request: greenlight_pb2.CloseChannelRequest,
        context: grpc.ServicerContext,
    ) -> greenlight_pb2.CloseChannelResponse: ...
    @abc.abstractmethod
    def CreateInvoice(
        self,
        request: greenlight_pb2.InvoiceRequest,
        context: grpc.ServicerContext,
    ) -> greenlight_pb2.Invoice:
        """Create a new invoice to receive an incoming payment."""
    @abc.abstractmethod
    def Pay(
        self,
        request: greenlight_pb2.PayRequest,
        context: grpc.ServicerContext,
    ) -> greenlight_pb2.Payment: ...
    @abc.abstractmethod
    def Keysend(
        self,
        request: greenlight_pb2.KeysendRequest,
        context: grpc.ServicerContext,
    ) -> greenlight_pb2.Payment:
        """Send a spontaneous payment, optionally with some extra information."""
    @abc.abstractmethod
    def ListPayments(
        self,
        request: greenlight_pb2.ListPaymentsRequest,
        context: grpc.ServicerContext,
    ) -> greenlight_pb2.ListPaymentsResponse:
        """Retrieve a list of payment performed by this node.

        The query can optionally be restricted to a single payment
        matching criteria that can be specified in the
        `ListPaymentsRequest`

        Notice: this does not include any payment that were
        received by this node, just the outgoing payments. Incoming
        payments can be retrieved using `ListInvoices`
        """
    @abc.abstractmethod
    def ListInvoices(
        self,
        request: greenlight_pb2.ListInvoicesRequest,
        context: grpc.ServicerContext,
    ) -> greenlight_pb2.ListInvoicesResponse:
        """Retrieve invoices that were created via CreateInvoice

        The query can optionally be restricted to only return a
        single invoice matching the given criteria.
        """
    @abc.abstractmethod
    def StreamIncoming(
        self,
        request: greenlight_pb2.StreamIncomingFilter,
        context: grpc.ServicerContext,
    ) -> collections.abc.Iterator[greenlight_pb2.IncomingPayment]:
        """Stream incoming payments

        Currently includes off-chain payments received matching an
        invoice or spontaneus paymens through keysend.
        """
    @abc.abstractmethod
    def StreamLog(
        self,
        request: greenlight_pb2.StreamLogRequest,
        context: grpc.ServicerContext,
    ) -> collections.abc.Iterator[greenlight_pb2.LogEntry]:
        """Stream the logs as they are produced by the node

        Mainly intended for debugging clients by tailing the log as
        they are written on the node. The logs start streaming from
        the first beginning, in order to allow inspection of events
        after an error occurred, That also means that the logs can
        be rather large, and should not be streamed onto
        resource-constrained devices.
        """
    @abc.abstractmethod
    def StreamHsmRequests(
        self,
        request: greenlight_pb2.Empty,
        context: grpc.ServicerContext,
    ) -> collections.abc.Iterator[greenlight_pb2.HsmRequest]:
        """////////////////////////////// HSM Messages ////////////////////////

        The following messages are related to communicating HSM
        requests back and forth. Chances are you won't need to
        interact with these at all, unless you want to embed the
        hsmd into your client. We recommend using a standalone hsmd
        such as hagrid, keeper of keys, to get started.

        Stream requests from the node to any key device that can
        respond to them.
        """
    @abc.abstractmethod
    def RespondHsmRequest(
        self,
        request: greenlight_pb2.HsmResponse,
        context: grpc.ServicerContext,
    ) -> greenlight_pb2.Empty: ...

def add_NodeServicer_to_server(servicer: NodeServicer, server: grpc.Server) -> None: ...

class HsmStub:
    def __init__(self, channel: grpc.Channel) -> None: ...
    Request: grpc.UnaryUnaryMultiCallable[
        greenlight_pb2.HsmRequest,
        greenlight_pb2.HsmResponse,
    ]
    Ping: grpc.UnaryUnaryMultiCallable[
        greenlight_pb2.Empty,
        greenlight_pb2.Empty,
    ]

class HsmServicer(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def Request(
        self,
        request: greenlight_pb2.HsmRequest,
        context: grpc.ServicerContext,
    ) -> greenlight_pb2.HsmResponse: ...
    @abc.abstractmethod
    def Ping(
        self,
        request: greenlight_pb2.Empty,
        context: grpc.ServicerContext,
    ) -> greenlight_pb2.Empty: ...

def add_HsmServicer_to_server(servicer: HsmServicer, server: grpc.Server) -> None: ...
